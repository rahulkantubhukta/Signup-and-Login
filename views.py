from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def signup(request):
    return render(request, "signup.html")
def login(request):
    fname1 = request.POST.get("fname")
    lname1=request.POST.get("lname")
    age1=request.POST.get("age")
    uniqueid1=request.POST.get("unique id")
    email1=request.POST.get("email")
    password4=request.POST.get("password1")
    password5=request.POST.get("password2")
    if password4==password5:
     return render(request, "login.html",{
     "First":fname1,
     "Last":lname1,
     "Age":age1,
     "Unique Id":uniqueid1,
     "Email":email1,
     "password4":password4
     })
    else:
     return HttpResponse("Your passwords are not matched , please reenter your passwords")