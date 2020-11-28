from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate, login,logout
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from.models import *
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def home(request):
    return render(request,'index.html')

def admin(request):
    if request.method =='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(username=name,password=password)
        if user:
            if name=="admin" and password=='admin123':

                login(request,user)
                return redirect(admin_home)
        else:
            return render(request,'login.html')
            

            
    else:
        return render(request,'login.html')

@user_passes_test(lambda u: u.is_superuser,login_url='/admin')
def admin_home(request):
    employees=Employee.objects.all()
    context={'employees':employees}
    return render(request,'admin.html',context)
@user_passes_test(lambda u: u.is_superuser,login_url='/admin')
def addemployee(request):
    if request.method =='POST':

        name=request.POST['name']
        phone=request.POST['phone']
        adress=request.POST['adress']
        email=request.POST['email']
        image=request.FILES.get('image')
        

        if Employee.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
            return render(request,'addemployee.html')


        elif Employee.objects.filter(phone=phone).exists():
            messages.info(request,"phone number already exists")
            return render(request,'addemployee.html')
            
        else:

            employee=Employee.objects.create(employee_name=name,email=email,phone=phone,adress=adress,image=image)
            employee.save()
            return redirect(admin_home)

    return render(request,'addemployee.html')

@user_passes_test(lambda u: u.is_superuser,login_url='/admin')
def editemployee(request,id):
    e=Employee.objects.get(id=id)
    if request.method =='POST':

        name=request.POST['name']
        phone=request.POST['phone']
        adress=request.POST['adress']
        email=request.POST['email']

        image=request.FILES.get('image')

        if 'image' not in request.POST:
            e.image=image
        else:
            e.image=e.image
        
        

        

        e.employee_name=name
        e.email=email
        e.phone=phone
        e.adress=adress
        e.save()
        return redirect(admin_home)
        

    return render(request,'updateemployee.html',{'e':e})
@user_passes_test(lambda u: u.is_superuser,login_url='/admin')
def deleteemployee(request,id):
    e=Employee.objects.get(id=id)
    e.delete();

    return redirect(admin_home)

@user_passes_test(lambda u: u.is_superuser,login_url='/admin')
def logout(request):
    auth.logout(request)
    return redirect('admin')