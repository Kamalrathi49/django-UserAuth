from django.shortcuts import redirect, render
from .forms import *
from myapp import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

@login_required
def home(request):
    users = CustomUser.objects.all()
    ctx = {'users':users}
    return render(request, 'home.html', ctx)

class Login( SuccessMessageMixin, auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_message = "Logged In successfully"

class SignUp( SuccessMessageMixin, generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('myapp:home')
    template_name = 'signup.html'
    success_message = "Your Account was created successfully, Please now login to access Home page"
    

def log_out(request):
    logout(request)
    messages.success(request, f"Logged out Successfully!")
    return redirect('/')


def deleteuser(request, customuser_id):
    user = CustomUser.objects.get(id = customuser_id)
    user.delete()
    messages.success(request, f"Account deleted Successfully!")
    return redirect('/')

