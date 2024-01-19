from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.
def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'GET':
        loginForm = LoginForm()
        return render(request, 'login.html' , {'form': loginForm})
    else:
        username = request.POST['username']
        password = request.POST['password']

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect(reverse('home'))
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))

def register_user(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
        else:
            return render(request, 'register.html', {'form': form})