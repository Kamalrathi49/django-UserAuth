from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model




class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
     'class': 'form-control', 'placeholder': 'Email Address'
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Address'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}),label=(u'Password'))
        
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'}),label=(u'Confirm Password'))

    class Meta:
        model = get_user_model()
        fields = ("username", "email", 'address', 'password1', 'password2' )
    
    def __init__(self, *args, **kwargs):
        # Call to ModelForm constructor
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'address', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))
