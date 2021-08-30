from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

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
            messages.success(request, f'Account created Successfully!')
            return redirect('/home')
        else:
            messages.error(request, f'Something went wrong! please try again.')
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
                messages.success(request, f'Logged in Successfully!')
                return redirect('/home')
            else:
                messages.error(request, f"Email or Password doesn't match! please try again.")
                return redirect('/')
        else:
            messages.error(request, f'Something went wrong! please try again.')
            return redirect('/')

    else:
        form = LoginForm()
        ctx = {'form':form}
        return render(request, 'login.html', ctx)

def log_out(request):
    logout(request)
    messages.success(request, f"Logged out Successfully!")
    return redirect('/')

# def updateuser(request, user_id,  ):
#     if request.method == 'POST':
#         inst = User.objects.get(id = user_id)
#         form = RegisterForm(request.POST or None, instance = inst)
#         if form.is_valid():
#             form.save()
#             extrafield.objects.create(
#                 address  = form.cleaned_data.get('address'),
#                 user = request.user
#             )
#             messages.success(request, f"Updated Successfully!")
#             return redirect('/home')

#         else:
#             messages.error(request, f'Something went wrong! please try again.')
#             return redirect('/home')
    
#     else:
#         inst = User.objects.get(id = user_id) + extrafield.objects.get(user__id = user_id)
#         form = RegisterForm(request.POST or None, instance = inst)
#         ctx = {'form': form}
#         return render(request, 'update_user.html', ctx)

def deleteuser(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    messages.success(request, f"User deleted Successfully!")
    return redirect('/')
