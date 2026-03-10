from django.urls import path
from patient import views

urlpatterns = [
    path('patients_d/', views.patients_d, name='patients_d'),
    path('p_a/', views.p_a, name='p_a'),
    path('patient_base',views.patient_base,name='patient_base'),
    path('update_pat/<int:updatePat_id>/',views.update_pat,name='update_pat'),
]