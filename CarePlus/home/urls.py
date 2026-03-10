from . import views
from django.urls import path



urlpatterns = [

    path('',views.index,name='index'),
    path('doctor/',views.doctor,name='doctor'),
    path('about/',views.about,name='about'),
    path('department/',views.department,name='department'),
    path('contact/',views.contact,name='contact'),

]