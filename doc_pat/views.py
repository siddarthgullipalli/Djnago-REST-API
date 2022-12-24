from django.shortcuts import render
from .models import patient

from django.urls import reverse_lazy

from django.views.generic.edit import UpdateView , CreateView, FormView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PatientCreate(CreateView , LoginRequiredMixin):
    model = patient
    fields = ['id','name','age']
    success_url = reverse_lazy('doctorpage')

    def from_valid(self,form):
        form.instance.user = self.request.user
        return super(PatientCreate).form_valid(form)

class Patientlist(ListView , LoginRequiredMixin):
    model = patient
    context_object_name = 'patients'

class Disease(UpdateView , LoginRequiredMixin):
    model = patient
    fields = ['Disease','Prescription']
    success_url = reverse_lazy('Patientlist')

    def from_valid(self,form):
        form.instance.user = self.request.user
        return super(Disease).form_valid(form)


class RegisterPage(FormView ):
    template_name = 'doc_pat/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('doctorpage')

    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(RegisterPage , self).form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'doc_pat/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) :
        return reverse_lazy('doctorpage')

class mainpage(LoginRequiredMixin):
    def doctorpage(request):
        return render(request, 'doc_pat/doc.html')


class Patient(DetailView):
    model = patient











