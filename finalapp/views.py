from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm
def home(request):
    documents = Document.objects.all()
    return render(request, 'finalapp/home.html', { 'documents': documents })

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

# Create your views here.
