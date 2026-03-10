from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import Patient1, Doctor
from django.contrib.auth.decorators import login_required
from admin1.models import Staff
from admin1.models import Invoice
from django.views.decorators.http import condition
from patient.models import Appoint
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from home.models import Emergency


# Create your views here.
@login_required
def admin2(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    doc = Doctor.objects.all()
    count = 0
    for i in doc:
        if i.is_approved:
            count += 1
    pat = Patient1.objects.all()
    st = Staff.objects.count()
    emer = Emergency.objects.count()

    context = {
        'pat':pat,
        'doc':doc,
        'count':count,
        'st':st,
        'emer':emer,
    }

    return render(request, 'adm.html', context)

def appointments(request):
    appoint = Appoint.objects.all()
    context = {
        'appoint':appoint,
    }
    return render(request, 'appointments.html', context)

def doctor_page(request):
    doc = Doctor.objects.all()
    count = 0
    for i in doc:
        if not i.is_approved:
            count += 1

    st = Staff.objects.count()

    context = {
        'count':count,
        'doc':doc,
        'st':st
    }
    return render(request, 'doctor_page.html', context)

def emergency(request):
    emer = Emergency.objects.all()


    context = {
        'emer':emer,

    }
    return render(request, 'emergency.html', context)

def doctor_req(request):
    doc = Doctor.objects.all()

    return render(request, 'doctor_req.html',{'doc':doc})

def doctor_list(request):
    doc = Doctor.objects.all()
    return render(request, 'doctor_list.html',{'doc':doc})

def patient_list(request):
    pat = Patient1.objects.all()
    return render(request, 'patient_list.html', {'pat':pat})

def doctor_approve(request, doctor_id):
    doct = Doctor.objects.get(id=doctor_id)
    doct.is_approved = True
    doct.save()
    return redirect('doctor_req')

def delete_doc(request, delete_id):
    doctor = Doctor.objects.get(id=delete_id)
    doctor.delete()
    messages.success(request, 'Account deleted successfully')
    return redirect('doctor_list')


def staff(request):
    if request.method == 'POST':
        firstname  = request.POST['firstname']
        lastname  = request.POST['lastname']
        contact  = request.POST['contact']
        address  = request.POST['address']
        jod  = request.POST['jod']
        ward  = request.POST['ward']
        gender  = request.POST['gender']
        age  = request.POST['age']

        Staff.objects.create(
            firstname=firstname,
            lastname=lastname,
            contact=contact,
            address=address,
            jod=jod,
            ward=ward,
            gender=gender,
            age=age,
        )
        messages.success(request, 'Added staff successfully..')
        return redirect('staff')

    st = Staff.objects.all().order_by('-jod')
    return render(request, 'staff.html', {'st':st})

def department1(request):
    ortho = Doctor.objects.filter(department='Orthopedics')
    emer = Doctor.objects.filter(department='Emergency')
    cardio = Doctor.objects.filter(department='Cardiology')
    neuro = Doctor.objects.filter(department='Neurology')
    ent = Doctor.objects.filter(department='ENT')
    derma = Doctor.objects.filter(department='Dermatology')
    radio = Doctor.objects.filter(department='Radiology')
    gs = Doctor.objects.filter(department='General Surgery')

    context={
        'ortho':ortho,
        'emer':emer,
        'cardio':cardio,
        'neuro':neuro,
        'ent':ent,
        'derma':derma,
        'radio':radio,
        'gs':gs,
    }
    return render(request, 'department1.html', context)

def invoice(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        admission_date = request.POST['admission_date']
        discharge_date = request.POST['discharge_date']
        treatment_details = request.POST['treatment_details']
        doctor_name = request.POST['doctor_name']
        amount = request.POST['amount']


        Invoice.objects.create(
            patient_name=patient_name,
            admission_date=admission_date,
            discharge_date=discharge_date,
            treatment_details=treatment_details,
            doctor_name=doctor_name,
            amount=amount,
            patient_id=None,
            id=None,

        )
        messages.success(request, 'Successfully bill generated')
        return redirect('inviews')

    return render(request, 'invoice.html')

def inviews(request):
    lr = Invoice.objects.order_by('-patient_id')[:1]

    context = {
        'lr':lr
    }
    return render(request, 'inviews.html', context)

def render_to_pdf(template_src, context_dict):
    # Render the HTML using Django's template system.
    template = render_to_string(template_src, context_dict)

    # Create an HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')

    # Generate the PDF; pisa.CreatePDF writes the output into the response object.
    pisa_status = pisa.CreatePDF(template, dest=response)

    # Return the PDF response if no error occurred, else return None.
    return response if not pisa_status.err else None

def pdf_view(request):
    lr = Invoice.objects.order_by('-discharge_date')[:1]

    context = {
        'lr': lr
    }
    return render_to_pdf('down_invoice.html', context)


def pdf_download_view(request):
    # Generate the PDF.
    response = pdf_view(request)
    if response:
        # Set Content-Disposition header to prompt the browser to download the file.
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    return response

def adm_base(request):
    doc = Doctor.objects.all()
    count = 0
    for i in doc:
        if i.is_approved:
            count += 1
    pat = Patient1.objects.all()
    st = Staff.objects.count()

    context = {
        'pat': pat,
        'doc': doc,
        'count': count,
        'st':st
    }
    return render(request, 'adm_base.html', context)

