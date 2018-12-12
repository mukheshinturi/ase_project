from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import os

from .models import Document
from .forms import DocumentForm
def home(request):
    return render(request, 'finalapp/home.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.user = request.user

            formInstance.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'finalapp/model_form_upload.html', {
        'form': form
    })
def searchdata(request):
     if request.method=="GET":
         key=request.GET.get('searchword')
         searchedlist=Document.objects.filter(Q(category__icontains=key) | Q(name__icontains = key))
         items=[]
         context={'items':searchedlist}

     return render(request,'myapp/category/index.html',context)
