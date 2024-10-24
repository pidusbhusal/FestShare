from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import EventSponser
from events.models import Event




def BeSponser(req):
    if req.method == 'POST':
        eventId = req.POST.get('event_id')
        return render(req, 'AddSponser.html', {'eventId' :eventId})

# Create your views here.
def AddSponser(req):
    if req.method == 'POST':
        company_name = req.POST.get('companyName')
        company_email = req.POST.get('companyEmail')
        title = req.POST.get('title')
        description = req.POST.get('description')  # Assuming you want to save this too
        event_id = req.POST.get('event_id')
        
        event = get_object_or_404(Event, id=event_id)
        # Create a new EventSponser instance
        new_sponser = EventSponser(
            sponserUser = req.user,
            company_name=company_name,
            company_email=company_email,
            title=title,
            offer=description ,
            sponseringEvent = event,
        )
        new_sponser.save()  # Save the new sponsor to the database

        # Optionally, add a success message
        messages.success(req, "Sponsor added successfully!")
        return redirect('/Home')
   
    return render(req, 'AddSponser.html')

