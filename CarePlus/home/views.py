from django.shortcuts import render
from home.models import Emergency
# Create your views here.
def index(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        contact = request.POST['contact']
        date = request.POST['date']
        email = request.POST['email']
        message = request.POST['message']

        Emergency.objects.create(
            patient_name=patient_name,
            contact=contact,
            date=date,
            email=email,
            message=message,
            doctor_name=None

        )

    return render(request, 'index.html')

def doctor(request):
    return render(request, 'doctor.html')

def about(request):
    return render(request, 'about.html')

def department(request):
    return render(request, 'department.html')

def contact(request):
    return render(request, 'contact.html')