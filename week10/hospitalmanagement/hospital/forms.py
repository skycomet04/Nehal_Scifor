from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','department','mobile','status','resident','fees']
class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','gender','mobile','email','address','status']
class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor','patient','ap_date','ap_time']

class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model = invoice
        fields = ['app','amount','services','qty','address','admit_date','discharge_date','remarks']



