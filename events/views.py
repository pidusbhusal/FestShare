from django.shortcuts import render, redirect
from .models import Event  # Import your Event model
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.
def Onboarding(req):
    if req.user.is_authenticated:
        return redirect('/Home')
    
    return render(req, 'Onboarding.html')

def Home(req):
    if not  req.user.is_authenticated:
        return redirect('/Login')
    
    events = Event.objects.all()

    return render(req, 'Home.html', {'events': events})

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
        ticket_price = req.POST.get('tickPrice')
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


def join_event(request, event_id):
    if request.method == "POST":
        event = Event.objects.get(id=event_id)
        if event.participants < event.max_participants:
            event.participants += 1
            event.save()
            return redirect('Home')  # Redirect back to the event list page after joining
    return HttpResponse("Unable to join the event.", status=400)