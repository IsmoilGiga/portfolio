from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProjectForm
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def redirect_to_login(request):
    return redirect('login')


@login_required
def home(request):
    projects = Project.objects.all().order_by('-id') 
    return render(request, 'home.html', {'projects': projects})


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


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Project added successfully") 
            return redirect('home') 
        else:
            print("Form errors:", form.errors) 
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})


def delete_project(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return JsonResponse({'success': True, 'message': 'Proyekt muvaffaqiyatli o‘chirildi'})
    return JsonResponse({'success': False, 'message': 'Proyektni o‘chirishda xato yuz berdi'})

@login_required
def delete_avatar(request):
    if request.method == 'POST':
        user_profile = request.user.profile
        user_profile.avatar = None
        user_profile.save()
        return JsonResponse({'success': True}) 
    return JsonResponse({'success': False}) 