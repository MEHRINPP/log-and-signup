from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
def loginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
         login(request,user)
         return redirect('success')
         
        
        else:
          return redirect('signup')
    return render(request,'login.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken.")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already registered.")
            return redirect('signup')    

        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Account created successfully!")
        return redirect('login')
    return render(request,'signup.html')
@login_required
@never_cache
def success(request):
   return render(request,'success.html')
def custom_logout(request):
   logout(request)
   return redirect('signup')

