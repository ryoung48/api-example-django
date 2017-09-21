import datetime
from django.db import models
from django.utils import timezone

# TODO: Fix timezone issue


def current_time():
    return timezone.now()


class Doctor(models.Model):
    status_options = (
        ("I", "checked-in"),
        ("O", "checked-out"),
        ("P", "with patient")
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=status_options)
    status_start = models.DateTimeField(default=current_time())
    api_id = models.IntegerField(default=-1)

    def update_status(self, status):
        self.status = status
        self.status_start = current_time()
        self.save()

    def jsonify(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
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
    gender = models.CharField(max_length=30, default="")
    doctor_id = models.IntegerField(default=-1)
    address = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    zip_code = models.CharField(max_length=15, default="")
    ethnicity = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    home_phone = models.CharField(max_length=30, default="")
    cell_phone = models.CharField(max_length=30, default="")
    preferred_language = models.CharField(max_length=3, default="")
    api_id = models.IntegerField(default=-1)

    def set_demographics(self, form):
        self.city = form['city']
        self.state = form['state']
        self.zip_code = form['zip_code']
        self.ethnicity = form['ethnicity']
        self.home_phone = form['home_phone']
        self.cell_phone = form['cell_phone']
        self.email = form['email']
        self.save()

    def jsonify(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "ssn": self.ssn,
            "gender": self.gender,
            "doctor": self.doctor_id,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "home_phone": self.home_phone,
            "cell_phone": self.cell_phone,
            "email": self.email,
            "ethnicity": self.ethnicity
        }

    def __str__(self):
        return self.first_name + " " + self.last_name


class Appointment(models.Model):
    status_options = (
        ("N", ""),
        ("A", "Arrived"),
        ("Ci", "Checked In"),
        ("Ir", "In Room"),
        ("Ca", "Cancelled"),
        ("F", "Complete"),
        ("C", "Confirmed"),
        ("Is", "In Session"),
        ("Ns", "No Show"),
        ("Nc", "Not Confirmed"),
        ("R", "Rescheduled")
    )
    status_map = {k: v for v, k in status_options}
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    office = models.IntegerField(default=-1)
    exam_room = models.IntegerField(default=-1)
    duration = models.IntegerField(default=-1)
    status = models.CharField(max_length=2, choices=status_options)
    reason = models.CharField(max_length=30)
    scheduled_date = models.DateTimeField(default=current_time())
    arrival_date = models.DateTimeField(default=current_time())
    wait_time = models.IntegerField(default=0)
    api_id = models.IntegerField(default=-1)

    def verify_patient(self, form):
        return self.patient.first_name == form['first_name'] and self.patient.last_name == form['last_name'] \
               and self.patient.ssn == form['ssn']

    def arrived(self):
        self.status = "A"
        self.arrival_date = current_time()
        self.save()

    def visit(self):
        self.status = "Is"
        self.wait_time = (current_time() - self.arrival_date).seconds
        self.save()

    def jsonify(self):
        return {
            "id": self.id,
            "reason": self.reason,
            "status": self.get_status_display(),
            "arrival_date": self.arrival_date.strftime("%Y-%m-%d %H:%M:%S"),
            "scheduled_time": self.scheduled_date.strftime("%Y-%m-%d %H:%M:%S"),
            "patient": self.patient.jsonify(),
            "wait_time": self.wait_time,
            "duration": self.duration,
            "office": self.office,
            "exam_room": self.exam_room,
            "doctor": self.doctor.api_id
        }

    def __str__(self):
        return self.reason
