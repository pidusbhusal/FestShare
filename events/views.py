from django.shortcuts import render, redirect
from .models import Event  # Import your Event model
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

    return render(req, 'Home.html')
def join_event(request, event_id):
    if request.method == "POST":
        event = Event.objects.get(id=event_id)
        if event.participants < event.max_participants:
            event.participants += 1
            event.save()
            return redirect('Home')  # Redirect back to the event list page after joining
    return HttpResponse("Unable to join the event.", status=400)
