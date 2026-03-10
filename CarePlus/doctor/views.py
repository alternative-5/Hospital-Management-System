from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from accounts.models import Doctor
from patient.models import Appoint
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def doc(request):
    doctor = request.user.doctor
    appoint = Appoint.objects.filter(doctor=doctor)
    count = 0

    for i in appoint:
        if not i.is_approved:
            count += 1

    cp = 0
    for i in appoint:
        if i.is_approved:
            cp += 1
    context = {
        'doctor':doctor,
        'count':count,
        'cp':cp,
    }
    return render(request, 'doct.html', context)

def update_doc(request, update_id):
    doctor = Doctor.objects.get(id=update_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')


        doctor.username = username
        doctor.firstname = firstname
        doctor.lastname = lastname
        doctor.email = email


        doctor.save()
        messages.success(request, 'Account updated successfully')
        return redirect('/doc')

    context = {'doctor': doctor}

    return render(request, 'edit_doc.html',context)
def doc_base(request):
    doctor = Doctor.objects.all()
    appoint = Appoint.objects.all()


    context = {
        'doctor': doctor,
        'appoint': appoint,


    }
    return render(request, 'doc_base.html',context)

# def delete_doc(request, delete_id):
#
#     doctor = Doctor.objects.get(id=delete_id)
#     doctor.delete()
#     messages.success(request, 'Account deleted successfully')
#     return redirect('index')

def appoint_table(request):

    doctor = request.user.doctor
    appoint = Appoint.objects.filter(doctor=doctor)
    doc = Doctor.objects.all()

    count = 0

    for i in appoint:
        if not i.is_approved:
            count += 1

    cp = 0
    for i in appoint:
        if i.is_approved:
            cp += 1

    context = {
        'appoint': appoint,
        'doctor': doctor,
        'doc': doc,
        'cp': cp,
        'count': count,

    }


    return render(request, 'appoint_table.html',context)

def appoint_approve(request, appoint_id):
    doct = Appoint.objects.get(id=appoint_id)
    doct.is_approved = True
    doct.save()
    return redirect('appoint_table')

def doct_patient(request):
    doctor = request.user.doctor
    appoint = Appoint.objects.filter(doctor=doctor)
    count = 0

    for i in appoint:
        if not i.is_approved:
            count += 1
    cp = 0
    for i in appoint:
        if i.is_approved:
            cp += 1
    context = {
        'doctor':doctor,
        'appoint':appoint,
        'cp':cp,
        'count':count,
    }
    return render(request, 'doct_patient.html', context)