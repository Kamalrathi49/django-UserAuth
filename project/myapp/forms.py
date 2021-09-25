from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import DateInput
from .models import *


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
     'class': 'form-control', 'placeholder': 'Email Address'
    }))

    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
     'class': 'form-control', 'placeholder': 'Phone No.'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}),label=(u'Password'))
        
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'}),label=(u'Confirm Password'))

    class Meta:
        model = get_user_model()
        fields = ("username", "email", 'date_of_birth', 'phone_number', 'password1', 'password2' )

        widgets = {
        'date_of_birth': DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date Of Birth'})
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ["username", "email", 'date_of_birth', 'phone_number', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))

    