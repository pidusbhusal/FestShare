from django.shortcuts import render, redirect, get_object_or_404
from .models import Event  # Import your Event model
from django.contrib import messages
import os
from django.conf import settings

from django.http import HttpResponse


# Create your views here.
def Onboarding(req):
    if req.user.is_authenticated:
        return redirect('/Home')
    
    return render(req, 'Onboarding.html')

def Home(req):
    if not  req.user.is_authenticated:
        return redirect('/Login')
    
    has_events = Event.objects.filter(organizer=req.user).exists() if req.user.is_authenticated else False
    events = Event.objects.all()
    context = { 
        'events': events,
        'has_events':has_events
    }
    

    return render(req, 'Home.html',context)

def Chat(req):
    if not  req.user.is_authenticated:
        return redirect('/Login')
    
    return render(req,'Chat.html') 

def AddEvent(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        event_description = req.POST.get('description')
        date = req.POST.get('eventTime')
        location = req.POST.get('eventLocation')
        image = req.FILES.get('image') 
        ticket_price = req.POST.get('ticketPrice')
        max_people = req.POST.get('maxNumberOfPeople')
    
        event = Event.objects.create(
            organizer=req.user,
            title=title,
            eventDescription=event_description,
            date=date,
            location=location,
            image=image,
            ticketPrice=ticket_price,
            maxNumberOfPeople=max_people
        )
        event.save()
        messages.success(req, 'Event Added Successfully')
        return redirect('/Home')

        
    return render(req, 'AddEvent.html')


def joinEvent(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        event = get_object_or_404(Event, id=event_id)
        organizer = event.organizername
        date = event.date
        title = event.title
        image = event.image.url
        description = event.eventDescription
        participant = event.participants
        maxparticipant = event.maxNumberOfPeople
        price  = event.ticketPrice
        return render(request , 'JoinEventCheckout.html', {'event_id':event_id,  'organizer' :organizer, 'date':date, 'title':title, 'image':image, 'description':description, 'participant':participant, 'maxparticipant':maxparticipant , 'price':price})


def ProceedToCheckout(req):
    if req.method == 'POST':
        event_id = req.POST.get('event_id')
        
        event = get_object_or_404(Event, id=event_id)

        user = req.user
        if user not in event.participants.all():
            event.participants.add(user)  # Add the user to participants
            event.save()
        messages.success(req,"Particiapted to the event sucessfully")
        return redirect("/Home")

    
    return render(req, "JoinEventCheckout.html")


def yourEvent(req):
    organizerEvent = Event.objects.filter(organizer = req.user)
    context = {'events':organizerEvent}
    return render(req, "YourEvent.html", context )

def delete_event(req, event_id):
    event = get_object_or_404(Event, id=event_id, organizer=req.user)
    
    if req.method == 'POST':
        if event.image:
            image_path = os.path.join(settings.MEDIA_ROOT, event.image.name)
            if os.path.isfile(image_path):
                os.remove(image_path)
        event.delete()
        messages.success(req, "Event deleted successfully.")
        return redirect('/YourEvent')  # Redirect to the page listing the user's events

    return redirect('/YourEvent')  # Redirect if the method is not POST (should not happen)