from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.


def home(request):
    users = User.objects.all()
    ctx = {'users':users}
    return render(request, 'home.html', ctx)

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            extrafield.objects.create(
                address  = form.cleaned_data.get('address'),
                user = request.user
            )
            return redirect('/home')
        else:
            return redirect('/signup')
    else: 
        form = RegisterForm()
        ctx = {'form': form}
        return render(request, 'signup.html', ctx)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                auth_login(request, user)
                return redirect('/home')
            else:
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = LoginForm()
        ctx = {'form':form}
        return render(request, 'login.html', ctx)

def log_out(request):
    logout(request)
    return redirect('/')