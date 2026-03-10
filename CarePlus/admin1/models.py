from django.db import models
from django.db.models import Count

# Create your models here.
class Staff(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=200)
    jod = models.DateField()
    ward = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    admission_date = models.DateField()
    discharge_date = models.DateTimeField()
    treatment_details = models.CharField(max_length=400)
    doctor_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    patient_id = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Count existing instances for this location
        data_counter = Invoice.objects.filter(patient_name=self.patient_name).aggregate(counter=Count('id'))['counter'] or 0
        # Increment the counter for the new instance
        data_counter += 1
        # Set the property_number using the new counter
        self.patient_id = f"{self.patient_name}-{data_counter:04d}"
        super(Invoice, self).save(*args, **kwargs)




