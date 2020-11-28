from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def admin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=auth(username=name,password=password)
        if user:
            login(request,user)
            return render(request,'admin.html')
            
            

    return render(request,'login.html')
