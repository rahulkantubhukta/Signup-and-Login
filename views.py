from django.shortcuts import render
from django.http import HttpResponse
from signup.views import login
# Create your views here.
def login(request):
    return render(request,"login.html")
def info(request):
    password6=request.POST.get("password3")
    email3=request.POST.get("email2")
    if email3==email1 and password6==password4:
         return render(request, "info.html")
    else:
         HttpResponse("Please enter a valid Email and Password")