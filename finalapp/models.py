from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from homepage import models as model1
# Create your models here.
class Document(models.Model):
    category_choices=(
    ('Objects','Objects'),
    ('Animals','Animals'),
    ('Abstract','Abstract'),
    ('Festivals','Festivals'),
    ('Food','Food'),
    ('Lifestyle','Lifestyle'),
    ('Nature','Nature'),
    ('People','People'),
    )
    name= models.CharField(max_length=150,default="string")
    category= models.CharField(max_length=150,default="string",choices=category_choices)
    #file1= models.CharField(max_length=1500,default="string")
    image=models.ImageField(default='',upload_to='')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(default='0')
    total_image_downloads=models.IntegerField(default='0')
    id=models.OneToOneField(model1.UserProfileInfo,on_delete='CASCADE')
