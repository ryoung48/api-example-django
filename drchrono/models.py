from django.db import models
from django.utils import timezone


class Doctor(models.Model):
    status_options = (
        ("I", "checked-in"),
        ("O", "checked-out"),
        ("P", "with patient")
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=status_options)
    status_start = models.DateTimeField()

    def update_status(self, status):
        self.status = status
        self.save()

    def jsonify(self):
        return {
            "first": self.first_name,
            "last": self.last_name,
            "id": self.id,
            "status": self.get_status_display(),
            "status_code": self.status,
            "time": self.status_start.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return self.first_name + " " + self.last_name


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ssn = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)

    def set_demographics(self, form):
        self.city = form['city']
        self.state = form['state']
        self.ethnicity = form['ethnicity']
        self.save()

    def jsonify(self):
        return {
            "first": self.first_name,
            "last": self.last_name,
            "ssn": self.ssn,
            "city": self.city,
            "state": self.state,
            "ethnicity": self.ethnicity
        }

    def __str__(self):
        return self.first_name + " " + self.last_name


class Appointment(models.Model):
    status_options = (
        ("A", "arrived"),
        ("C", "confirmed"),
        ("F", "finished")
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_options)
    reason = models.CharField(max_length=30)
    scheduled_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    wait_time = models.IntegerField()

    def verify_patient(self, form):
        return self.patient.first_name == form['first'] and self.patient.last_name == form['last'] \
               and self.patient.ssn == form['ssn']

    def arrived(self):
        self.status = "A"
        self.arrival_date = timezone.now()
        self.save()

    def visit(self):
        self.status = "F"
        self.wait_time = (timezone.now() - self.arrival_date).seconds
        self.save()

    def jsonify(self):
        return {
            "id": self.id,
            "reason": self.reason,
            "status": self.get_status_display(),
            "arrival_date": self.arrival_date.strftime("%Y-%m-%d %H:%M:%S"),
            "scheduled_date": self.scheduled_date.strftime("%Y-%m-%d %H:%M:%S"),
            "patient": self.patient.jsonify(),
            "wait_time": self.wait_time
        }

    def __str__(self):
        return self.reason
