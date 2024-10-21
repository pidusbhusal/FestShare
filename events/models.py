from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    date = models.DateField()
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    eventDescription = models.TextField()
    image = models.ImageField(upload_to='event_images/')  # Set the upload path for images
    ticketPrice = models.FloatField()
    maxNumberOfPeople = models.IntegerField()

    @property
    def organizername(self):
        return self.user.first_name  # Access the user's first name

    def __str__(self):
        return f"{self.title} organized by {self.organizername}"
