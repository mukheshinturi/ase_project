from django.shortcuts import render
from homepage.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'homepage/index.html')

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password) #hashing the password
            user.save() #save hash password to database
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=UserForm()
    return render(request,'homepage/registration.html',{'user_form':user_form,'registered':registered})

@login_required
def special(request):
    return HttpResponse("You are logged in dude")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print("username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'homepage/login.html')
