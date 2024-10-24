from django.db import models
from django.contrib.auth.models import User
from events.models import Event

# Create your models here.

class EventSponser(models.Model):
    sponseringEvent = models.ForeignKey(Event, related_name="events_sponsers", on_delete=models.CASCADE)
    sponserUser  = models.ForeignKey(User, on_delete=models.CASCADE) 
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    title = models.CharField(max_length=100)
    offer = models.TextField()

    def __str__(self):
        return f"{self.title} by {self.company_name}"