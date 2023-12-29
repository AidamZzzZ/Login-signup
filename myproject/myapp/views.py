from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm


def index(request):
    return render(request, 'auth/index.html')

def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auth:login")
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form':form})
    

def user_login(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("auth:home")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect("auth:login")