from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('project', views.project, name='project'),
    path('#contact', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_project, name='add_project')
]
