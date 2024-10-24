from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    eventDescription = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    ticketPrice = models.FloatField()
    maxNumberOfPeople = models.IntegerField()
    participants = models.ManyToManyField(User, related_name='event_participants', blank=True)

    @property
    def organizername(self):
        return self.organizer.first_name

    def __str__(self):
        return f"{self.title} organized by {self.organizername}"
