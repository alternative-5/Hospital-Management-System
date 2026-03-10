from django.urls import path
from . import views


urlpatterns = [
    path('doc_login/',views.doc_login, name='doc_login'),
    path('admin_login/',views.admin_login, name='admin_login'),
    path('patient_login/',views.patient_login, name='patient_login'),
    path('patient_register/',views.patient_register, name='patient_register'),
    path('doc_register/',views.doc_register, name='doc_register'),
    path('message_click/',views.message_click, name='message_click'),
    path('logout1/',views.logout1,name='logout1')
]