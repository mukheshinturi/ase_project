from django.db import models
from django.contrib.auth.models import User
from django import forms
class UserProfileInfo(models.Model):
<<<<<<< HEAD
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=250,default="x")
    city=models.CharField(max_length=80,default="x")
    phone=models.IntegerField(max_length=12,default=12345)
=======
    user=models.ForeignKey(User,on_delete='PROTECT')
>>>>>>> e2e81602d85c6bebcced2f293e90e4ff77cb60f6

    def __str__(self):
        return self.user.username
class feedback(models.Model):
    name=models.CharField(max_length=250)
    rating=models.CharField(max_length=2)
    text=models.CharField(max_length=250)
<<<<<<< HEAD

    def __str__(self):
        return self.name
=======
>>>>>>> e2e81602d85c6bebcced2f293e90e4ff77cb60f6
