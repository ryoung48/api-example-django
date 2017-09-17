from django.http import JsonResponse
from django.middleware import csrf
import json

from django.views.decorators.csrf import csrf_exempt

from .models import Doctor, Appointment, Patient


def doctors(request):
    doctor_list = Doctor.objects.order_by('-first_name')
    return JsonResponse({
        "checked_in": [doctor.jsonify() for doctor in doctor_list if doctor.status != "O"],
        "checked_out": [doctor.jsonify() for doctor in doctor_list if doctor.status == "O"]
    })


@csrf_exempt
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


@csrf_exempt
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
