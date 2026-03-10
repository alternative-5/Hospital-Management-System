from django.db import models

# Create your models here.
class Emergency(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    contact = models.IntegerField()
    date = models.DateField()
    email = models.EmailField()
    message = models.CharField(max_length=400)
    doctor_name = models.CharField(max_length=255, blank=True)