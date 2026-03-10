from contextlib import nullcontext

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patient.models import Appoint
from accounts.models import Doctor, Patient1


# Create your views here.

@login_required
def patients_d(request):

    patient = request.user.patient1
    appoint = Appoint.objects.filter(patient_name=patient)
    pat = Patient1.objects.all()

    pt = Doctor.objects.all()
    context = {
        'pt':pt,
        'patient':patient,
        'appoint':appoint,
        'pat':pat,
    }
    return render(request, 'patient.html',context)

def p_a(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        contact = request.POST['contact']
        address = request.POST['address']
        appoint_date = request.POST['appoint_date']
        dob = request.POST['dob']
        doctor_department = request.POST['doctor_department']
        doctor = request.POST['doctor']
        purpose = request.POST['purpose']

        Appoint.objects.create(
            patient_name=patient_name,
            contact=contact,
            address=address,
            appoint_date=appoint_date,
            dob=dob,
            doctor_department=doctor_department,
            doctor=doctor,
            purpose=purpose,
            is_approved=False,
            note=nullcontext
        )
        messages.success(request, 'Appointment sent successfully')
        return redirect('patients_d')
    patient  = request.user.patient1
    pt = Doctor.objects.all()
    context = {
        'pt':pt,
        'patient':patient
    }
    return render(request, 'appoint_patient.html',context)


def patient_base(request):


    patient = Patient1.objects.all()
    pt = Doctor.objects.all()



    context = {
        'pt':pt,
        'patient':patient,

    }

    return render(request, 'patient_base.html',context)
def update_pat(request, updatePat_id):
    patient = Patient1.objects.get(id=updatePat_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')


        patient.username = username
        patient.firstname = firstname
        patient.lastname = lastname
        patient.email = email


        patient.save()
        messages.success(request, 'Account updated successfully')
        return redirect('/patients_d')

    context = {'patient': patient}

    return render(request, 'patient_edit.html',context)