from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='img/profile-img.jpg')

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255,)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField()

    def __str__(self):
        return self.title