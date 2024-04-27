from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
from.models import Doctor,Patient,Appointment,invoice
from datetime import date
from django.db.models import Q
from .utils import table_exists
def createdoctor(request):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    if request.method =='POST':
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewdoctor')
    else:
        form = CreateDoctorForm()
    return render(request, 'createdoctor.html', {'form': form})

def createappointment(request):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff ')
        return redirect('log_in')
    doc=Doctor.objects.all()
    pat=Patient.objects.all()
    if request.method =='POST':
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            ap_instance=form.save(commit=False)
            ap_instance.doc_fee=ap_instance.doctor.fees
            ap_instance.save()
            return redirect('receipt')
    else:
        form = CreateAppointmentForm()
    context={'form':form,'doc_list':doc,'pat_list':pat}        
    return render(request,'create.html',context)

def createpatient(request):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff')
        return redirect('log_in')
    if request.method =='POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewpatient')
    else:
        form = CreateDoctorForm()
    return render(request,'createpatient.html',{'form':form})

def dashboard(request):
    doc=Doctor.objects.filter(Q(status='Available') | Q(status='Resident'))
    p_date=date.today()
    pdate=str(p_date)
    if p_date.month==1:
        p_y=p_date.year-1
        p_m=12
    else:
        p_y=p_date.year
    if p_date.day<=7 and p_date.month in [1,3,5,7,8,10,12]:
        p_m=p_date.month-1
        p_d=31+(p_date.day-7)
    elif p_date.day<=7 and p_date.month==2:
        p_m=p_date.month-1
        p_d=28+(p_date.day-7)
    elif p_date.day<=7 and p_date.month in [4,6,9,11]:
        p_m=p_date.month-1
        p_d=30+(p_date.day-7) 
    else:
        p_d=p_date.day
        p_m=p_date.month
    p_d=p_date.day-7
    p_date1=date(p_y,p_m,p_d)
    p_date1=str(p_date1)
    app=Appointment.objects.filter(ap_date__range=[p_date1, pdate])
    tapp=app.count()
    tdoc=doc.count()
    t_pat=Patient.objects.all().count()
    context={'doc_list':doc,'appoint_list':app,'tapp':tapp,'tdoc':tdoc,'t_pat':t_pat}
    return render(request,'dashboard.html',context)

def deleteappoint(request,aid):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff.You cannot delete appointment')
        return redirect('log_in')
    delapp=Appointment.objects.get(id=aid)
    delapp.delete()
    return redirect('viewappointment')

def deletedoctor(request,did):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff.You cannot delete doctor')
        return redirect('log_in')
    deldoc=Doctor.objects.get(id=did)
    deldoc.delete()
    return redirect('viewdoctor')

def deletepatient(request,pid):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff. You cannot delete patient')
        return redirect('log_in')
    delpat=Patient.objects.get(id=pid)
    delpat.delete()
    return redirect('viewpatient')

def delete_receipt(request, id):
    queryset = invoice.objects.get(id=id)
    queryset.delete()
    return redirect('viewappointment')

def invoices(request):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    ap=Appointment.objects.all().order_by("-ap_date")
    inv=""
    if request.method=='POST':
        form = CreateInvoiceForm(request.POST)
        print(form.errors)
        if form.is_valid():
            instance=form.save(commit=False)
            app=Appointment.objects.get(id=request.POST['app'])
            instance.treating_doctor=app.doctor.name
            instance.patient_name=app.patient.name
            instance.department=app.doctor.department
            qty = int(request.POST['qty'])
            instance.total_amount=qty*app.doc_fee
            instance.mobile=app.patient.mobile
            instance.age=app.patient.age
            instance.gender=app.patient.gender
            instance.save()
            return redirect('receipt')
        else:
            messages.error(request,"There was issue while creating invoice .Please try again later")
    if request.method =="GET":
        inv=invoice.objects.last()
    context={'appoint':ap,'invoice':inv.app}
    return render(request,'receipt.html',context)

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html')
def log_out(request):
    logout(request)
    return redirect('log_in')

def doctor_detail(request,did):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    doc=Doctor.objects.get(id=did)
    context={'type':'doctor','doctor':doc}
    return render(request,'detail.html',context)

def patient_detail(request,pid):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    pat=Patient.objects.get(id=pid)
    context={'type':'patient','patient':pat}
    return render(request,'detail.html',context)

def app_detail(request,aid):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    appoint=Appointment.objects.get(id=aid)
    context={'type':'appoint','appointment':appoint}
    return render(request,'detail.html',context)

def viewdoctor(request):
    doc=Doctor.objects.all().order_by('name')
    context={'doc_list':doc}
    return render(request, 'viewdoctor.html',context)

def viewinvoice(request,id):
    total_sum=0
    queryset=""
    if request.method=='GET':
        app=Appointment.objects.get(id=id)
        if app!=None:
            queryset = invoice.objects.filter(app=app)
            total_sum = sum(receipt.total_amount for receipt in queryset)
    context={'items':queryset,'grand_total':total_sum,'app_id':id}
    return render(request,'viewreceipt.html',context)

def generateinvoice(request,id):
    total_sum=0
    queryset=""
    inv=""
    bill_date=date.today()
    if request.method=='GET':
        app=Appointment.objects.get(id=id)
        if app!=None:
            queryset = invoice.objects.filter(app=app)
            inv=invoice.objects.filter(app=app)[:1]
            total_sum = sum(receipt.total_amount for receipt in queryset)
    context={'items':queryset,'grand_total':total_sum,'invoice':inv,'billing_date':bill_date}
    return render(request,'generate_invoice.html',context)

def viewpatient(request):
    if not request.user.is_staff:
        messages.info(request, f'You are not authorised staff to view this page')
        return redirect('log_in')
    patient=Patient.objects.all().order_by('name')
    context={"pat_list":patient}    
    return render(request, 'viewpatient.html', context)
def viewappointment(request):
    appoint=Appointment.objects.all().order_by('ap_date','ap_time')
    context={"appoint_list":appoint}   
    return render(request, 'viewappointment.html', context)

def updatedoctor(request,did):
        ditem=Doctor.objects.get(id=did)
        form=CreateDoctorForm(instance=ditem)       
        if request.method =='POST':
            form=CreateDoctorForm(request.POST, instance=ditem)
            if form.is_valid():
                form.save()
                return redirect('viewdoctor')
        else:
            form = CreatePatientForm(instance=ditem)
        return render(request,'updatedoctor.html',{'task':form})

def update_patient(request,pid):
        item=Patient.objects.get(id=pid)
        form=CreatePatientForm(instance=item)       
        if request.method =='POST':
            form=CreatePatientForm(request.POST, instance=item)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('viewpatient')
        else:
            form = CreatePatientForm(instance=item)
        return render(request,'updatepatient.html',{'task':form})



