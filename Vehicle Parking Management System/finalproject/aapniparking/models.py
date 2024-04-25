from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

type=[("4","4-wheeler"),("3","3-wheeler"),("2","2-wheeler")]

class ParkingSpace(models.Model):
    no = models.BigAutoField(unique=True,primary_key=True)
    veh_type = models.CharField(max_length=255,choices=type)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.no}-{self.veh_type}"
    
class Vehicle(models.Model):
    veh_registration_no=models.CharField(max_length=10)
    veh_model=models.CharField(max_length=255)
    owner=models.CharField(max_length=200,default='dev')
    contact=models.CharField(max_length=10,validators=[RegexValidator(regex=r'^[6-9]\d{9}$',message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")])
    vehicle_category=models.CharField(max_length=50,choices=type,default="2")
    remark=models.TextField(blank=True)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    parked=models.BooleanField(default=False)
    def __str__(self):
        return self.veh_registration_no

class ParkingBookSlot(models.Model):
    vehicle_uniqueid=models.ForeignKey(Vehicle,related_name='vehicle_uniqueid',on_delete=models.CASCADE)
    veh_model=models.CharField(max_length=255)
    slot_no=models.ForeignKey(ParkingSpace,on_delete=models.SET_NULL,null=True)
    owner_name=models.CharField(max_length=255)
    veh_registration=models.CharField(max_length=10)
    owner_contactno=models.CharField(max_length=10,null=True,blank=True)
    parking_rate=models.PositiveIntegerField()
    intime=models.DateTimeField(auto_now_add=True)
    outtime=models.DateTimeField(null=True,blank=True)
    fee=models.FloatField(null=True,blank=True)
    vehicle_type=models.CharField(max_length=50,choices=type,default="2")
    booking_user=models.ForeignKey(User,on_delete=models.CASCADE)
    parking_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.owner_name}"
    def save(self,*args,**kwargs):
        if self.vehicle_type=='4':
           self.parking_rate=50
        elif self.vehicle_type=='3':
            self.parking_rate=30
        elif self.vehicle_type=='2':
            self.parking_rate=20
        if self.outtime!=None:
            timediff=(self.outtime-self.intime).total_seconds()/60
            if timediff<=360:
                self.fee=self.parking_rate
            elif timediff>360:
                rate=self.parking_rate/(6*60)
                self.fee=round(rate*(timediff-360)+self.parking_rate,3)
        if self.outtime==None:
            ins=Vehicle.objects.get(id=self.vehicle_uniqueid.id)
            ins.parked=True
            space_ins=ParkingSpace.objects.get(no=self.slot_no.no)
            ins.save()
            if space_ins:
                space_ins.is_available=False
                space_ins.save()
        elif self.outtime:
            ins=Vehicle.objects.get(id=self.vehicle_uniqueid.id)
            space_ins=ParkingSpace.objects.get(no=self.slot_no.no)
            space_ins.is_available=True
            space_ins.save()
            ins.parked=False
            ins.save()
        super().save(*args,**kwargs)
    

        
