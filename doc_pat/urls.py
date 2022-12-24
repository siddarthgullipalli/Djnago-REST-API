from django.urls import path
from .views import PatientCreate ,Disease , RegisterPage , CustomLoginView , mainpage , Patientlist , Patient
from django.contrib.auth.views import LogoutView

from .import views


urlpatterns = [
    path('create',PatientCreate.as_view(),name='Patient_create'),
    path('disease/<int:pk>/',Disease.as_view() , name='disease'),
    path('register/',RegisterPage.as_view(), name='Register'),
    path('login/',CustomLoginView.as_view(),name='Login'),
    path('',mainpage.doctorpage,name='doctorpage'),
    path('logout/',LogoutView.as_view(next_page='Login'),name='Logout'),
    path('list/',Patientlist.as_view(),name='Patientlist'),
    path('<int:pk>/',Patient.as_view(),name='Prescription'),
]
