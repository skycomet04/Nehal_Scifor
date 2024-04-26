from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from portfolio.models import Contact
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

# Create your views here.
