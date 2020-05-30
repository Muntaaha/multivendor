# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User 
from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Customer
        fields = ['name', 'email', 'password1', 'password2']

