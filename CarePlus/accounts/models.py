from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count



# Create your models here

class Doctor(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=20)
    jod = models.DateField()
    profile = models.ImageField(upload_to='doctor_profile')
    password = models.CharField(max_length=50)
    is_doctor = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True,blank=True)
    previous_login = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.firstname


class Patient1(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField()
    contact = models.IntegerField()
    aadhar_no = models.IntegerField()
    address = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='patient_profile')
    password = models.CharField(max_length=50)
    is_patient = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    previous_login = models.DateTimeField(null=True, blank=True)
    patient_id = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Count existing instances for this location
        data_counter = Patient1.objects.filter(firstname=self.firstname).aggregate(counter=Count('id'))['counter'] or 0
        # Increment the counter for the new instance
        data_counter += 1
        # Set the property_number using the new counter
        self.patient_id = f"{self.firstname}-{data_counter:04d}"
        super(Patient1, self).save(*args, **kwargs)

    def __str__(self):
        return self.firstname


