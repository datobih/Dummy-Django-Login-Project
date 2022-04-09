from django.shortcuts import render
from django.contrib.auth.models import User
from my_login_app.models import UserProfile
import sys

from pathlib import Path

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import login,logout

my_directory=Path(__file__).resolve().parent.parent
sys.path.append(my_directory)


from custom_auth_backend import MyEmailBackend
# Create your views here.
def index(request):


    return render(request,'my_login_app/index.html')


def registration_view(request):
    is_registered=False

    if request.method =="POST":
       
        full_name=request.POST.get('full_name')
        password=request.POST.get('password')
        email=request.POST.get('email')


        user=User()
        user.username=full_name
        user.set_password(password)
        user.email=email
        user.save()

        userProfile=UserProfile()
        userProfile.user=user
        userProfile.save()
        is_registered=True





    return render(request,'my_login_app/registration.html',{'is_registered':is_registered})


def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('my_login_app:login'))



def login_view(request):


    if(request.method =="POST"):

        email=request.POST.get('email')
        password=request.POST.get('password')

        user=MyEmailBackend.authenticate(request=request,username=email,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not Active.")

        else:
            return HttpResponse("Wrong login details provided.")



    else:
        return render(request,'my_login_app/login.html')


def profile_view(request):
    userProfile=UserProfile.objects.get(user=request.user)


    
    if request.method=="POST":
        if userProfile:
            profile_name=request.POST.get('name')
            profile_portfolio=request.POST.get('portfolio')
    
            profile_pic=request.FILES['profile_pic']

            
            if request.user.username!=profile_name:
                request.user.username=profile_name

            if userProfile.portfolio!=profile_portfolio:
                userProfile.portfolio=profile_portfolio

            if userProfile.profile_pic!=profile_pic:
                userProfile.profile_pic=profile_pic

            request.user.save()
            userProfile.save()


        
    if userProfile:
        name=userProfile.user.username
        email=userProfile.user.email
        portfolio=userProfile.portfolio

        return render(request,'my_login_app/profile.html',context={'profile_name':name,'profile_email':email,'portfolio':portfolio})
   
    