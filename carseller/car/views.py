
from django.contrib import messages

from django.shortcuts import render
from .models import contactus
# Create your views here.
def index(request):
    return render(request,'index.html')

def contactuss(request):
    return render(request,'contactus.html')

def contactsave(request):
    if request.method=="POST":
       finame=request.POST.get('fname')
       lname=request.POST.get('lname')
       country=request.POST.get('country')
       subject=request.POST.get('subject')
       c_data=contactus(finame=finame,lname=lname,country=country,subject=subject)
       c_data.save()
    return render(request, 'contactus.html')

# def savesignup(request):
#     if request.method=="POST":
#         fname=request.POST.get('s_fname')
#         lname=request.POST.get('s_lname')
#         email=request.POST.get('s_email')
#         psswd=request.POST.get('s_passwd')
#         c_data=Signup_login(fname=fname,lname=lname,email=email,psswd=psswd)
#         c_data.save()
#     return render(request, 'index.html')