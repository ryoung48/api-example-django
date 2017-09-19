import json

from django.utils import timezone
from django.test import TestCase

from .models import Doctor, Patient, Appointment


class AppointmentModelTests(TestCase):

    def test_was_verify_correct_patient(self):
        appointment = dummy_appointment()
        self.assertIs(appointment.verify_patient({
            "first": "Patient",
            "last": "Test",
            "ssn": "999333999"
        }), True)

    def test_patient_arrival(self):
        appointment = dummy_appointment()
        old_arrival = appointment.arrival_date
        appointment.arrived()
        self.assertIs(appointment.status, "A")
        self.assertIs(old_arrival < appointment.arrival_date, True)

    def test_patient_visit(self):
        appointment = dummy_appointment()
        appointment.visit()
        self.assertIs(appointment.status, "F")


class PatientModelTests(TestCase):

    def test_set_patient_demographics(self):
        patient = create_patient("Patient", "Test")
        patient.set_demographics({
            "city": "city",
            "state": "state",
            "ethnicity": "ethnicity"
        })
        self.assertIs(patient.city, "city")
        self.assertIs(patient.state, "state")
        self.assertIs(patient.ethnicity, "ethnicity")


class AppointmentFlowEndpointsTests(TestCase):

    def test_get_appointments(self):
        appointment = dummy_appointment()
        result = json.loads(self.client.get("http://localhost:8000/appointment/1/").content)
        self.assertIs(result["confirmed"][0]["id"], appointment.id)
        self.assertIs(bool(result["arrived"]), False)
        self.assertIs(bool(result["finished"]), False)
        self.assertIs(result["avg_wait"], 0)


class PatientFlowEndpointsTests(TestCase):

    def test_get_doctors(self):
        doctor1 = create_doctor("First", "Test")
        doctor2 = create_doctor("Second", "Test", status="O")
        result = json.loads(self.client.get("http://localhost:8000/doctors/").content)
        self.assertIs(result["checked_in"][0]["id"], doctor1.id)
        self.assertIs(result["checked_out"][0]["id"], doctor2.id)

    # def test_correct_identity_verification(self):
    #     appointment = dummy_appointment()
    #     response = self.client.post("http://localhost:8000/appointment/verify/", data={
    #         "doctor_id": appointment.doctor.id,
    #         "first": appointment.patient.first_name,
    #         "last": appointment.patient.last_name,
    #         "ssn": appointment.patient.ssn
    #     }).content
    #     print(response)
    #     result = json.loads(response)
    #     self.assertIs(result["status"], "info")
    #     self.assertIs(result["message"], "We found your appointment!")
    #     self.assertIs(result["patient"]["ssn"], appointment.patient.ssn)
    #     self.assertIs(result["appointment"], appointment.id)


def dummy_appointment():
    doctor = create_doctor("Dr", "Test")
    patient = create_patient("Patient", "Test")
    return creat_appointment(doctor, patient)


def create_doctor(first, last, status="I", status_start=timezone.now()):
    return Doctor.objects.create(first_name=first, last_name=last, status=status, status_start=status_start)


def create_patient(first, last, ssn="999333999"):
    return Patient.objects.create(first_name=first, last_name=last, ssn=ssn, state="", city="", ethnicity="")


def creat_appointment(doctor, patient, status="C", reason="", scheduled_date=timezone.now(),
                      arrival_date=timezone.now(), wait_time=0):
    return Appointment.objects.create(doctor=doctor, patient=patient, status=status, reason=reason,
                                      scheduled_date=scheduled_date, arrival_date=arrival_date, wait_time=wait_time)
