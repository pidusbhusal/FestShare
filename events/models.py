from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    date = models.DateField()
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    eventDescription = models.TextField()
    image = models.ImageField(upload_to='event_images/')  # Set the upload path for images
    ticketPrice = models.FloatField()
    maxNumberOfPeople = models.IntegerField()
    participants = models.ManyToManyField(User, related_name='event_participants', blank=True)  # Participants as ManyToManyField


    @property
    def organizername(self):
        return self.organizer.first_name  # Access the user's first name

    def __str__(self):
        return f"{self.title} organized by {self.organizername}"




class Sponsor(models.Model):  # Corrected spelling
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=300)  # Use snake_case for field names
    company_email = models.EmailField(max_length=300)  # Changed to EmailField for validation
    sponsor_message = models.TextField()

    def organizer_name(self):
        return self.organizer.first_name  # Access the user's first name
    
    def event_name(self):
        return self.event.title

    def __str__(self):
        return f"{self.event_name()} Sponsored By {self.organizer_name()}"