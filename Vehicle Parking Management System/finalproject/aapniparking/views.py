from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from .forms import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.http import FileResponse
from reportlab.pdfgen import canvas


@login_required
def addParkingSpace(request):
    if request.method=="POST":
        form=createParkingSlot(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "parking slot added successfully")
            return redirect('dashboard')
    else:
        form=createParkingSlot()
    context={'update':False}
    return render(request,'addparkingspace.html',context)

@login_required
def addVehicle(request):
    if not request.user.is_authenticated:
        messages.info(request, f'You are not logged in .Please login in to add vehicle ')
        return redirect('login')
    users=User.objects.all()
    if request.method=="POST":
        form=addVehicleForm(request.POST)
        if form.is_valid():
            ins=form.save(commit=False)
            ins.created_by=request.user
            ins.save()
            if not request.user.is_staff:
                subject = 'Parking Confirmed'
                message = f'Hi {request.user.username}!!, Your vehicle is added successfully.Thanks for using our parking service.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.user.email, ]
                send_mail( subject, message, email_from, recipient_list )
            messages.success(request, "vehicle added successfully")
            return redirect('dashboard')
        else:
             messages.error(request, "There was some issue while trying to add vehcile details.Please try again later")
    else:
        form=addVehicleForm
    context={'user':users,'form':form,'update':False}
    return render(request,'addvehicle.html',context)

@login_required
def bookingslot(request,sid=0):
    space=ParkingSpace.objects.filter(is_available=True)
    if not request.user.is_staff:
        vehicles=Vehicle.objects.filter(Q(created_by=request.user) & Q(parked=False))
        print(vehicles)
    else:
         vehicles=Vehicle.objects.filter(parked=False)
    space1=""
    if sid==0:
        id=False
    else:
        id=True
        space1=ParkingSpace.objects.get(no=sid)
    if request.method=="POST":
        form = addParkingForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if sid==0:
                slotins_no=request.POST['slot_no']
                slot_ins=ParkingSpace.objects.get(no=slotins_no)
                instance.slot_no=slot_ins
            else:
                instance.slot_no=space1     
            instance.owner_name=instance.vehicle_uniqueid.owner
            instance.veh_model=instance.vehicle_uniqueid.veh_model
            instance.veh_registration=instance.vehicle_uniqueid.veh_registration_no
            instance.owner_contactno=instance.vehicle_uniqueid.contact
            userid=request.user
            instance.booking_user=userid 
            instance.save()
            if not request.user.is_staff:
                subject = 'Parking Confirmed'
                message = f'Hi {userid.username}!!, Your booking slot is confirmed .Your parking slot_no is {instance.slot_no.no}.Thanks for using our parking service.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [userid.email, ]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, f"An email has been sent of booking confirmation on your registered email id")
            messages.success(request, f"Your booking slot is confirmed .Your parking slot_no is {instance.slot_no.no}.Thanks for using our parking service.")
            return redirect('dashboard')
        else:
            print(form.errors)
            messages.error(request, "There was some issue while trying to book slot.Please try again later")
    else:
        form= addParkingForm()
    context={'slots':space,'reg_no':vehicles,'id':id,'update':False,'slot':space1}
    return render(request,'bookparking.html',context)

def available_slots(request):
    slots=ParkingSpace.objects.filter(is_available=True)
    context={'slot_list':slots}
    return render(request,'available_slots.html',context)

def deleteparking(request,pid):
    delpark=ParkingBookSlot.objects.get(id=pid)
    no=delpark.slot_no.no
    slot=ParkingSpace.objects.get(no=no)
    slot.is_available=True
    slot.save()
    delpark.delete()
    return redirect('viewparking')

def deletevehicle(request,vid):
    delveh=Vehicle.objects.get(id=vid)
    delveh.delete()
    return redirect('viewvehicle')

def deletespace(request,sid):
    delspace=ParkingSpace.objects.get(no=sid)
    delspace.delete()
    return redirect('availableslot')

def deleteuser(request,uid):
    deluser=User.objects.get(id=uid)
    deluser.delete()
    return redirect('viewuser')

def generate_pdf(request,pid):
    bookslot= ParkingBookSlot.objects.get(id=pid)
    response = FileResponse(generate_pdf_file(pid), 
                            as_attachment=True, 
                            filename=f'{bookslot.owner_name}.pdf')
    return response
 
def generate_pdf_file(pid):
    from io import BytesIO
    buffer = BytesIO()
    f = canvas.Canvas(buffer)
    ticket = ParkingBookSlot.objects.get(id=pid)
    f.drawString(250, 750, "Parking Book Reciept")
 
    y = 700
    f.drawString(450, 750, f" Parking Date: {ticket.parking_date}")
    f.drawString(400, y, f"Vehicle Type: {ticket.vehicle_type}")
    f.drawString(50, y, f"Vehicle Registration No: {ticket.veh_registration}")
    f.drawString(50, y - 30, f"Vehicle Intime: {ticket.intime}")
    f.drawString(370, y - 30, f"Vehicle Intime: {ticket.outtime}")
    f.drawString(50, y - 60, f"Parking Slot No: {ticket.slot_no}")
    f.drawString(50, y - 90, f"Parking Rate: {ticket.parking_rate}")
    f.drawString(50, y - 120, f"Parking Total Amount: {ticket.fee}")
    f.drawString(400, y - 120, f"Amount Due: {ticket.fee}")
    f.drawString(50, y - 150, f"Rate is calculated: flat amount ={ticket.parking_rate} till 6hr addidtional hours= rs 8.33/hr ")
    y -= 180

    f.showPage()
    f.save()
 
    buffer.seek(0)
    return buffer

def todaybooking(request):
    if request.user.is_staff:
        parking_list=ParkingBookSlot.objects.filter(parking_date=date.today())
    else:
        messages.error(request,"Please sign in to view")
        return redirect('login') 
    context={'parkings':parking_list}
    return render(request,'viewparkings.html',context)

def parkingdetail(request,id):
    if not request.user.is_authenticated:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('login')
    parkings=ParkingBookSlot.objects.get(id=id)
    context={'type':'parking','parking':parkings}
    return render(request,'detail.html',context)

def vehicledetail(request,id):
    if not request.user.is_authenticated:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('login')
    vehicles=Vehicle.objects.get(id=id)
    context={'type':'vehicle','vehicle':vehicles}
    return render(request,'detail.html',context)

def spacedetail(request,id):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('login')
    spaces=ParkingSpace.objects.get(no=id)
    if spaces.is_available==False:
        bookslot=ParkingBookSlot.objects.get(slot_no=id)
    else:
        bookslot=""
    context={'type':'space','space':spaces,'booking':bookslot}
    return render(request,'detail.html',context)

def home(request):
    space=ParkingSpace.objects.filter(is_available=True)
    count_space=space.count()
    t_space=ParkingBookSlot.objects.all().count()
    parking=ParkingBookSlot.objects.filter(parking_date=date.today())
    if request.user.is_authenticated:
        if request.user.is_staff:
            total_users=User.objects.all().count()
            c_date=date.today()
            pdate=str(c_date)
            if c_date.month==1:
                p_y=c_date.year-1
                p_m=12
            else:
                p_y=c_date.year
            if c_date.day<=7 and c_date.month in [1,3,5,7,8,10,12]:
                p_m=c_date.month-1
                p_d=31+(c_date.day-7)
            elif c_date.day<=7 and c_date.month==2:
                p_m=c_date.month-1
                p_d=28+(c_date.day-7)
            elif c_date.day<=7 and c_date.month in [4,6,9,11]:
                p_m=c_date.month-1
                p_d=30+(c_date.day-7) 
            else:
                p_d=c_date.day
                p_m=c_date.month
            p_d=c_date.day-7
            p_date1=date(p_y,p_m,p_d)
            p_date1=str(p_date1)
            app=ParkingBookSlot.objects.filter(parking_date__range=[p_date1, pdate])
            days=app.count()
            parking=parking.count()
            context={'total':total_users,'available':count_space,'total_slots':t_space,'day':days,'parking':parking,'park_list':app}
        else:
            user_parking=ParkingBookSlot.objects.filter(booking_user=request.user.id)
            park_count=user_parking.count()
            context={'available':count_space,'total_slots':t_space,'my_parking':park_count} 
    else:
        context={'available':count_space,'total_slots':t_space}
    return render(request,'dashboard.html',context)

def view_parkings(request):
    if request.user.is_staff:
        parking_list=ParkingBookSlot.objects.all()
    elif request.user.is_authenticated and not request.user.is_staff:
        fullname=request.user.first_name+request.user.last_name
        parking_list=ParkingBookSlot.objects.filter(Q(booking_user=request.user) | Q(owner_name=fullname) | Q(owner_name=request.user.first_name))
    else:
        messages.error(request,"Please sign in to view")
        return redirect('login') 
    context={'parkings':parking_list}
    return render(request,'viewparkings.html',context)

def view_space(request):
    space_list=ParkingSpace.objects.all()
    context={'spaces':space_list}
    return render(request,'viewspace.html',context)

def view_user(request):
    if request.user.is_staff:
        user_list=User.objects.all()
    else:
        messages.error(request,"Please sign in to view")
        return redirect('login') 
    context={'users':user_list}
    return render(request,'viewusers.html',context)

def view_vehicles(request):
    if request.user.is_staff:
        vehicle_list=Vehicle.objects.all()
    elif request.user.is_authenticated and not request.user.is_staff:
        vehicle_list=Vehicle.objects.filter(created_by=request.user)
    else:
        messages.error(request,"Please sign in to view")
        return redirect('login') 
    context={'vehicles':vehicle_list}
    return render(request,'viewvehicles.html',context)

def update_parking(request,pid):
    parking=ParkingBookSlot.objects.get(id=pid)
    form=addParkingForm(instance=parking)
    if request.method=='POST':
        form=addParkingForm(request.POST,instance=parking)
        if form.is_valid():
            form.save()
            outtime=request.POST['outtime']
            if outtime!=None:
                ins_veh=Vehicle.objects.get(id=parking.vehicle_uniqueid.id)
                ins_veh.parked=False
                ins_veh.save()
            return redirect('viewparking')
        else:
            print(form.errors)
            messages.error(request, "There was some issue while trying to edit details.Please try again later")
    else:
        form=addParkingForm(instance=parking)
    context={"update":True,'parking':parking}
    return render(request,'bookparking.html',context)

def update_space(request,sid):
    space=ParkingSpace.objects.get(no=sid)
    form=createParkingSlot(instance=space)
    if request.method=='POST':
        form=createParkingSlot(request.POST,instance=space)
        if form.is_valid():
            form.save()
            return redirect('viewspace')
        else:
            print(form.errors)
            messages.error(request, "There was some issue while trying to edit details.Please try again later")
    else:
        form=createParkingSlot(instance=space)
    context={"update":True,'space':space}
    return render(request,'addparkingspace.html',context)

def update_vehicle(request,vid):
    vehicle=Vehicle.objects.get(id=vid)
    form=addVehicleForm(instance=vehicle)
    if request.method=='POST':
        form=addVehicleForm(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('viewvehicle')
        else:
            messages.error(request, "There was some issue while trying to edit details.Please try again later")
    else:
        form=addVehicleForm(instance=vehicle)
    context={"update":True,'vehicle':vehicle}
    return render(request,'addvehicle.html',context)

def userdetail(request,uid):
    if request.user.is_authenticated:
        user=User.objects.get(id=uid)
        context={'user':user}
        return render(request,'userdetail.html',context)
    else:
        messages.info(request,"you are not authorised to view this page") 
        return render(request,'userdetail.html')  
def log_in(request):
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"User doesn't exist. Please register yourself")
    return render(request,'login.html') 

def log_out(request):
    logout(request)
    return redirect('dashboard')

def register(request):
    if request.method=="POST":
        user=request.POST['user']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confpass']
        if confirm_password != password:
            messages.error(request,"password doesn't match")
            messages.info(request,"Failed to create user account.Please try again")
            return redirect('register')
        if User.objects.filter(username=user).exists():
            messages.error(request, "Username already taken. Please choose another username.")
            return redirect('register')
        else:
            try:
                user=User.objects.create_user(username=user,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                subject = 'Welcome to AapniParking'
                message = f'Hi {firstname}!!, your account is created successfully.Your username is {user}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, "User registered successfully. You can now login.")
                return redirect('login')
            except IntegrityError as e:
                messages.error(request, "Username already exists.Try login with the same username")
    return render(request,"register.html")
    
def  forget_password(request):
    if request.method=="POST":
        user=request.POST['user']
        password=request.POST['pass']
        confirm=request.POST['confirm']
        user=User.objects.get(username=user)
        if user is not None :
            if password==confirm:
                user.set_password(password)
                user.save()
                return redirect('login')
            else:
                return messages.warning(request,"Password doesn't match")
        else:
            return messages.warning(request,"There is no user with that username")
    return render(request,'forgetpassword.html')

