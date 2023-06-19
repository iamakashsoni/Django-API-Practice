from django.db import models

# Create your models here.

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    specialist = models.CharField(max_length=200)

class Patients(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    dob = models.DateField()
