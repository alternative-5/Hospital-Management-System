from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from accounts.models import Doctor, Patient1



# Create your views here.
def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('/admin2/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        print(user)

        if user is not None:
            login(request,user)
            return redirect('/admin2/')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('admin_login')

    return render(request, 'admin_login.html')

def doc_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contact = request.POST['contact']
        email = request.POST['email']
        department = request.POST['department']
        jod = request.POST['jod']
        profile = request.FILES['profile']
        password = request.POST['password']

        doctor_user = User.objects.create_user(username,email,password)
        doctor_user.firstname = firstname
        doctor_user.save()

        doc = Doctor(
            User=doctor_user,
            firstname=firstname,
            lastname=lastname,
            contact=contact,
            email=email,
            department=department,
            jod=jod,
            profile=profile,
            password=password,
            is_doctor=True,
            is_approved=False,
        )
        doc.save()
        messages.success(request,'Successfully Registered')
        return redirect('doc_login')
    return render(request, 'doc_register.html')

def doc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            try:
                doctor = Doctor.objects.get(User=user)
                if not doctor.is_approved:
                    messages.error(request, "Your account is not approved yet. Please wait.")
                    return redirect('doc_login')

                doctor.previous_login = doctor.last_login
                doctor.last_login = now()
                doctor.save()


                login(request, user)
                return redirect('doc')

            except Doctor.DoesNotExist:
                messages.error(request, "You are not registered as a Doctor.")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'doc_login.html')

def patient_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        dob = request.POST['dob']
        contact = request.POST['contact']
        aadhar_no = request.POST['aadhar_no']
        address = request.POST['address']
        password = request.POST['password']

        patient_user = User.objects.create_user(username,email,password)
        patient_user.firstname = firstname
        patient_user.save()

        pat = Patient1(
            User=patient_user,
            firstname=firstname,
            lastname=lastname,
            email=email,
            dob=dob,
            contact=contact,
            aadhar_no=aadhar_no,
            address=address,
            password=password,
            is_patient=True,
            is_approved=True,
        )
        pat.save()
        return redirect('patient_login')
    return render(request, 'patient_register.html')


def patient_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                # Ensure the authenticated user is a patient
                patient = Patient1.objects.get(User=user)

                # Log in the user
                login(request, user)
                return redirect('patients_d')  # Redirect to the home page after login

            except Patient1.DoesNotExist:
                # User is not registered as a patient
                messages.error(request, "You are not registered as a patient.")
        else:
            # Invalid username or password
            messages.error(request, "Invalid username or password.")

    return render(request, "patient_login.html")



def message_click(request):
    return render(request, 'message_click.html')


def logout1(request):
    logout(request)
    return redirect('index')