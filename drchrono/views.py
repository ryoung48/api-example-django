from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.middleware import csrf
import json
import requests

from django.shortcuts import render

from .models import Doctor, Appointment

# https://drchrono.com/api/appointments?since=2014-02-24T15:32:19


def api_request(request, endpoint):
    social = request.user.social_auth.get(provider='drchrono')
    response = requests.get('https://drchrono.com/api/' + endpoint, headers={
        'Authorization': 'Bearer %s' % social.extra_data['access_token'],
    })
    return response.json()


@login_required(login_url='/')
def secure(request):
    social = request.user.social_auth.get(provider='drchrono')
    response = requests.get('https://drchrono.com/api/doctors', headers={
        'Authorization': 'Bearer %s' % social.extra_data['access_token'],
    })
    return JsonResponse(response.json(), safe=False)


def home(request):
    print(request.user)
    return render(request, 'home.html')


@login_required(login_url='/')
def doctors_api(request):
    doctor_list = api_request(request, "doctors")
    return JsonResponse({
        "checked_in": doctor_list["results"],
        "checked_out": []
    })


@login_required(login_url='/')
def patients_api(request):
    patients_list = api_request(request, "patients")
    print(patients_list)
    return JsonResponse({
        "checked_in": patients_list["results"],
        "checked_out": []
    })


@login_required(login_url='/')
def appointments_api(request):
    appointments_list = api_request(request, "appointments?since=2016-09-17 02:03:16")
    print(appointments_list)
    return JsonResponse({
        "checked_in": appointments_list["results"],
        "checked_out": []
    })


def doctors(request):
    doctor_list = Doctor.objects.order_by('-first_name')
    return JsonResponse({
        "checked_in": [doctor.jsonify() for doctor in doctor_list if doctor.status != "O"],
        "checked_out": [doctor.jsonify() for doctor in doctor_list if doctor.status == "O"]
    })


def get_appointments(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor)
    finsihed = [appointment.jsonify() for appointment in appointments if appointment.status == "F"]
    return JsonResponse({
        "confirmed": [appointment.jsonify() for appointment in appointments if appointment.status == "C"],
        "arrived": [appointment.jsonify() for appointment in appointments if appointment.status == "A"],
        "finished": finsihed,
        "avg_wait": sum([
            appointment.wait_time for appointment in appointments if appointment.status == "F"
        ], 0) / (len(finsihed) if finsihed else 1)
    })


def doctor_status_update(request):
    form = json.loads(request.body)
    doctor = Doctor.objects.get(pk=form['doctor_id'])
    doctor.update_status(form['status'])
    return JsonResponse(doctor.jsonify())


def visit(request):
    form = json.loads(request.body)
    appointment = Appointment.objects.get(pk=form['appointment_id'])
    appointment.visit()
    return JsonResponse({})


def verify_identity(request):
    form = json.loads(request.body)
    doctor = Doctor.objects.get(pk=form['doctor_id'])
    appointments = Appointment.objects.filter(doctor=doctor)
    found = [appointment for appointment in appointments if appointment.verify_patient(form)]
    return JsonResponse({
        "status": "info" if found else "error",
        "message": "We found your appointment!" if found else "We could not find your appointment.",
        "patient": found[0].patient.jsonify() if found else {},
        "appointment":  found[0].id if found else -1
    })


def finalize_checkin(request):
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
