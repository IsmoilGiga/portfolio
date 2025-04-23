from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def redirect_to_login(request):
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')



def project(request):
    return render(request, 'project.html')


def contact(request):
    if request.method == "POST":
        name == request.POST['name']
        email == request.POST['email']
        subject == request.POST['subject']
        message == request.POST['message']
        contact = models.Home(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'home.html')