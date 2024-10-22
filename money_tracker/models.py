from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastname = models.CharField(max_length= 100)
    email = models.EmailField(max_length=200)
    preferences = models.TextField()
    NetWorth = models.IntegerField(default=0)

    def __str__(self):
        return self.firstName + ' ' + self.lastname 
    
class Event(models.Model):
    uploader = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    participants = models.IntegerField(default=0)
    max_participants = models.IntegerField(default=30)

    def __str__(self):
        return self.title