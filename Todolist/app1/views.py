from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate,login as django_login , logout as django_logout
from django.contrib.auth.decorators import login_required
from app1.models import Task



# Create your views here.
def login(request):
        if request.method =="POST":
            username=request.POST['login_username']
            password=request.POST['login_password']
            print(username,password)
            user= authenticate(username=username,password=password)
            print(user)
            if user is not None:
                django_login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        return render(request,'loginpage.html')

def forgot(request):
        return render(request,'forgot.html')

def signup(request):
        if request.method =="POST":
            firstname=request.POST['signup_firstname']
            lastname=request.POST['signup_lastname']
            username=request.POST['signup_username']
            password=request.POST['signup_password']
            confirmpassword=request.POST['signup_confirm_password']
            email=request.POST['signup_email']
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                print('user created')
                return redirect('login')
        return render(request,'signup.html')

def logout(request):
     django_logout(request)
     return redirect('login')


@login_required(login_url='login')
def home(request):
        contect ={'sucess':False}
        if request.method =="POST":
            title=request.POST['title']
            description=request.POST['desc']
            print(title,description)
            task=Task(Title=title, Description=description)
            task.save(title=title,description=description)
            contect ={'sucess':True}
            messages.info(request,'Task Added Successfully')
        return render(request,'index.html' ,contect)