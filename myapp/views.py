from django.shortcuts import render
from finalapp.models import Document
import os
from django.conf import settings

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#import pathlib
def index(request,value):
    image_list=Document.objects.filter(category=value)
    items=[]
    listitems=[]

    page = request.GET.get('page', 1)
    paginator = Paginator(image_list, 12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context={'users': users,'value':value}

    return render(request, 'myapp/category/index.html', context)


def category(request):
    return render(request,'myapp/category/category.html')
