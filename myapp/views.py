from django.shortcuts import render, redirect
from finalapp.models import Document
from django.http import HttpResponse
from django.contrib.auth import logout
import os
from django.conf import settings

# Create your views here.
#import pathlib
def index(request,value):
    p=Document.objects.filter(category=value)
    items=[]
    listitems=[]

    context={'items':p}
    return render(request, 'myapp/category/index.html', context)
def user(request,value):
    p = Document.objects.filter(user=value)
    print(Document.objects.filter(user=value))
    context={'items':p}
    return render(request, 'myapp/category/user.html', context)

def countlikes(request,likeid):
    if request.method=='GET':
        if likeid:
            likedata=Document.objects.get(image=likeid)
            pre_likes = likedata.likes
            pre_likes += 1
            likedata.likes = pre_likes
            likedata.save()
    return HttpResponse('you have liked the image...please go back for more images')


def category(request):
    return render(request,'myapp/category/category.html')

def user_logout(request):
    logout(request)
    return redirect('finalapp:home')
