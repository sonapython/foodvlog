from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password1=request.POST['password1']
        user=auth.authenticate(username=username,password1=password1)
        return redirect('/')
    else:
       return render(request,"login.html")

def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        username=request.POST['username']
        password=request.POST['password']
        psw2=request.POST['psw-repeat']
        email=request.POST['email']
        user=User.objects.create_user(username=username,email=email,password=password,firstname=firstname)
        user.save();
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')