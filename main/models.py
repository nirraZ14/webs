from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class Foryou(models.Model):
    things=models.CharField(max_length=100)
    thingdesc=models.CharField(max_length=1000)
    thingimg=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.things}"


class Service(models.Model):
    img=models.CharField(max_length=1000)
    title=models.CharField(max_length=40)
    body=models.CharField(max_length=100)
    foryou=models.ManyToManyField(Foryou,blank=True, related_name="for_you")
    def __str__(self):
        return f"{self.title}"
    

    
class Works(models.Model):
    workIt=models.CharField(max_length=40)
    imgUrl=models.CharField(max_length=1000)
    explore=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.workIt}"
class Gallery(models.Model):
    galleryUrl=models.CharField(max_length=1000)



class Blog(models.Model):
    blogimg=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    content=models.CharField(max_length=1000)
    blogUrl=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title} made by {self.author}"
