

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.http import JsonResponse
from django.middleware import csrf
import json
import requests
from django.shortcuts import redirect

from drchrono import settings
from .models import Doctor, Appointment, Patient, current_time


# TODO: Error check get_appointments, doctor_status_update, visit, verify_patient_identity, & finalize_patient_checkin


def api_request(request, endpoint):
    social = request.user.social_auth.get(provider='drchrono')
    response = requests.get('https://drchrono.com/api/' + endpoint, headers={
        'Authorization': 'Bearer %s' % social.extra_data['access_token'],
    })
    return response.json()


def api_update(request, endpoint, payload):
    social = request.user.social_auth.get(provider='drchrono')
    response = requests.post('https://drchrono.com/api/' + endpoint, data=payload, headers={
        'Authorization': 'Bearer %s' % social.extra_data['access_token'],
    })
    return response.json()


def logged_in(request):
    return JsonResponse({
        "user": str(request.user)
    })


def logout_user(request):
    if str(request.user) != 'AnonymousUser':
        user = api_request(request, "/users/current")
        doctor_status_update(user, status='O')
        logout(request)
    return redirect(settings.LOGIN_URL)


def cache_doctors(user, request):
    doctor = Doctor.objects.filter(api_id=user["doctor"])
    if not doctor:
        info = api_request(request, "doctors")["results"]
        found = [d for d in info if d["id"] == user["doctor"]]
        if found:
            Doctor.objects.create(
                first_name=found[0]["first_name"],
                last_name=found[0]["last_name"],
                status="O",
                api_id=user["doctor"]
            )


def cache_patients(user, request):
    patients = api_request(request, "patients?doctor=" + str(user["doctor"]))["results"]
    for patient in patients:
        local = Patient.objects.filter(api_id=patient["id"])
        if not local:
            Patient.objects.create(
                first_name=patient["first_name"],
                last_name=patient["last_name"],
                ssn=patient["social_security_number"] if patient["social_security_number"] else '',
                gender=patient["gender"] if patient["gender"] else 'Other',
                city=patient["city"] if patient["city"] else '',
                state=patient["state"] if patient["state"] else '',
                ethnicity=patient["ethnicity"],
                doctor_id=patient["doctor"],
                api_id=patient["id"]
            )


def cache_appointments(user, request):
    appointments = api_request(
        request,
        "appointments?since=2014-02-24T15:32:19&doctor=" + str(user["doctor"])
    )["results"]
    for appointment in appointments:
        local = Appointment.objects.filter(api_id=appointment["id"])
        status = appointment["status"] if appointment["status"] else ''
        if not local:
            doctor = Doctor.objects.filter(api_id=appointment["doctor"])[0]
            patient = Patient.objects.filter(api_id=appointment["patient"])[0]
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                office=appointment["office"],
                duration=appointment["duration"],
                exam_room=appointment["exam_room"],
                reason=appointment["reason"],
                status=Appointment.status_map[status],
                api_id=appointment["id"]
            )


@login_required
def build_kiosk(request):
    user = api_request(request, "/users/current")
    if user["is_doctor"]:
        cache_doctors(user, request)
        doctor_status_update(user, status='I')
        cache_patients(user, request)
        cache_appointments(user, request)
    return redirect(settings.LOGIN_URL)


@login_required
def get_appointments(request):
    user = api_request(request, "/users/current")
    doctor = Doctor.objects.filter(api_id=user["doctor"])[0]
    appointments = Appointment.objects.filter(doctor=doctor)
    finsihed = [appointment.jsonify() for appointment in appointments if appointment.status == "F"]
    in_progress = [appointment.jsonify() for appointment in appointments if appointment.status == "Is"]
    return JsonResponse({
        "doctor": doctor.jsonify(),
        "confirmed": [appointment.jsonify() for appointment in appointments if appointment.status == "C"],
        "arrived": [appointment.jsonify() for appointment in appointments if appointment.status == "A"],
        "session": in_progress,
        "finished": finsihed,
        "avg_wait": sum([
            appointment.wait_time for appointment in appointments if any(appointment.status == c for c in ["F", "Is"])
        ], 0) / (len(in_progress + finsihed) if (in_progress or finsihed) else 1)
    })


def doctors(request):
    doctor_list = Doctor.objects.order_by('-first_name')
    return JsonResponse({
        "checked_in": [doctor.jsonify() for doctor in doctor_list if doctor.status != "O"],
        "checked_out": [doctor.jsonify() for doctor in doctor_list if doctor.status == "O"]
    })


def doctor_status_update(user, status='O'):
    doctor = Doctor.objects.filter(api_id=user["doctor"])[0]
    doctor.update_status(status)


def visit(request):
    form = json.loads(request.body)
    appointment = Appointment.objects.get(pk=form['appointment_id'])
    patient = appointment.patient
    patient_json = patient.jsonify()
    patient_json["id"] = patient.api_id
    api_update(request, "/patients", patient_json)
    appointment_json = appointment.jsonify()
    appointment_json["id"] = appointment.api_id
    appointment_json["patient"] = appointment.patient.api_id
    api_update(request, "/appointments", appointment_json)
    appointment.visit()
    return JsonResponse({})


def verify_patient_identity(request):
    form = json.loads(request.body)
    if 'doctor_id' in form:
        doctor = Doctor.objects.get(pk=form['doctor_id'])
        appointments = Appointment.objects.filter(doctor=doctor)
    else:
        appointments = Appointment.objects.all()
    found = sorted(
        [appointment for appointment in appointments if appointment.verify_patient(form) and appointment.status != 'F'],
        key=lambda x: abs(x.scheduled_date - current_time())
    )
    return JsonResponse({
        "status": "info" if found else "error",
        "message": "We found your appointment!" if found else "We could not find your appointment.",
        "patient": found[0].patient.jsonify() if found else {},
        "appointment":  found[0].id if found else -1
    })


def finalize_patient_checkin(request):
    form = json.loads(request.body)
    appointment = Appointment.objects.get(pk=form['appointment'])
    appointment.patient.set_demographics(form)
    appointment.arrived()
    return JsonResponse({
        "status": "success",
        "message": "You have been checked-in successfully!"
    })


def get_csrf_token(request):
    token = csrf.get_token(request)
    return JsonResponse({'token': token})
