from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Vaccination(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    child_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    hospital = models.CharField(max_length=250)
    child_age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=25)
class Hospital(models.Model):
    name = models.CharField(max_length=250,blank=True, null=True)
    place = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField()
    contact = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.name or f"Hospital {self.id}"

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=250, blank=True, null=True)
    type = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.vaccine_name or f"Vaccine {self.id}"


class Appointment(models.Model):
    date = models.DateField(blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

class Complaint(models.Model):
    user = models.ForeignKey(Vaccination, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250, blank=True, null=True)
    complaint = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    replay = models.CharField(max_length=2000, blank=True, null=True)
    # Create your models here.

class Book_Appointment(models.Model):
    user = models.ForeignKey(Vaccination, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    vaccine_name = models.CharField(max_length=250, blank=True, null=True)
    vaccinated = models.BooleanField(default=False)
    card = models.IntegerField(default=0)

class Report_Card(models.Model):
    user = models.ForeignKey(Vaccination,on_delete=models.CASCADE)
    child_age = models.IntegerField()
    date = models.DateField()
    vaccine = models.CharField(max_length=200)