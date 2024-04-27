from django.db import models
from datetime import date

class Doctor(models.Model):
    name=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    mobile=models.IntegerField()
    status=models.CharField(max_length=150)
    doctor_ap_date=models.DateField(auto_now=True)
    fees=models.IntegerField(default=350)
    resident=models.TextField(default="-")
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField(null=True)
    address=models.CharField(max_length=250)
    status=models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    ap_date=models.DateField()
    ap_time=models.TimeField()
    doc_fee=models.IntegerField(default=350)
    def __str__(self):
        return str(self.patient)

class invoice(models.Model):
    app=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    treating_doctor=models.CharField(max_length=255)
    patient_name=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    amount=models.PositiveIntegerField()
    qty=models.PositiveIntegerField()
    services=models.TextField()
    admit_date=models.DateField(blank=True,null=True)
    discharge_date=models.DateField(blank=True,null=True)
    address=models.CharField(max_length=250)
    mobile=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    status=models.CharField(max_length=150)
    bill_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    total_amount=models.PositiveIntegerField()
    remarks=models.TextField(null=True,blank=True)
    def __str__(self):
         return str(self.services)