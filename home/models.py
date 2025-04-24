from django.db import models

# Create your models here.
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