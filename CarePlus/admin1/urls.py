from django.urls import path
from . import views


urlpatterns = [
    path('admin2/',views.admin2,name='admin2'),
    path('adm_base/',views.adm_base,name='adm_base'),
    path('appointment/',views.appointments,name='appointments'),
    path('doctor_page/',views.doctor_page,name='doctor_page'),
    path('emergency/',views.emergency,name='emergency'),
    path('doctor_req/',views.doctor_req,name='doctor_req'),
    path('doctor_list/',views.doctor_list,name='doctor_list'),
    path('patient_list/',views.patient_list,name='patient_list'),
    path('department1/',views.department1,name='department1'),
    path('invoice/',views.invoice,name='invoice'),
    path('inviews/',views.inviews,name='inviews'),
    path('staff/',views.staff,name='staff'),
    path('doctor_approve/<int:doctor_id>/',views.doctor_approve,name='doctor_approve'),
    path('delete_doc/<int:delete_id>/',views.delete_doc, name='delete_doc'),
    path('view_pdf/', views.pdf_view, name='view_pdf'),
    path('download_pdf/', views.pdf_download_view, name='download_pdf'),


]