from django import forms
from django.contrib.auth.models import User
from homepage.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password')
