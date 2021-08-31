from django.contrib.messages.api import error
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    users = CustomUser.objects.all()
    ctx = {'users':users}
    return render(request, 'home.html', ctx)


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'



    
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Account created Successfully!')
            return redirect('/home')
        else:
            messages.error(request, f'Something went wrong! please try again.')
            return redirect('/signup')
    else: 
        form = RegisterForm()
        ctx = {'form': form}
        return render(request, 'signup.html', ctx)

class login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'

def log_out(request):
    logout(request)
    messages.success(request, f"Logged out Successfully!")
    return redirect('/')

def updateuser(request, customuser_id):
    if request.method == 'POST':
        inst = CustomUser.objects.get(id = customuser_id)
        form = RegisterForm(request.POST or None, instance = inst)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f"Updated Successfully!")
            return redirect('/home')
        else:
            messages.error(request, "something went wrong, please try again!")
            return redirect(f'/update_user/{customuser_id}')
    
    else:
        inst = CustomUser.objects.get(id = customuser_id)
        form = RegisterForm(request.POST or None, instance = inst)
        ctx = {'form': form}
        return render(request, 'update_user.html', ctx)

def deleteuser(request, customuser_id):
    user = CustomUser.objects.get(id = customuser_id)
    user.delete()
    messages.success(request, f"User deleted Successfully!")
    return redirect('/')
