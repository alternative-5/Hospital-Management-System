from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import Doctor
# Create your models here.

class Appoint(models.Model):
        patient_name = models.CharField(max_length=50)
        contact = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(10)])
        address = models.CharField(max_length=100)
        appoint_date = models.DateField()
        dob = models.DateField()
        doctor_department = models.CharField(max_length=200)
        doctor = models.CharField(max_length=200)
        purpose = models.CharField(max_length=200)
        is_approved = models.BooleanField(default=False)
        note = models.CharField(max_length=100)

