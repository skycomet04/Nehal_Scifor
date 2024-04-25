from .models import *
from django import forms
from django.contrib.auth.models import User

class addParkingForm(forms.ModelForm):
    class Meta:
        model=ParkingBookSlot
        fields=['vehicle_uniqueid','outtime','vehicle_type']

class addVehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['veh_registration_no','veh_model','owner','contact','vehicle_category','remark','parked']

class createParkingSlot(forms.ModelForm):
    class Meta:
        model=ParkingSpace
        fields=['veh_type','is_available']