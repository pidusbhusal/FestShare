from django.shortcuts import render, redirect
from .models import Event  # Import your Event model


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

def PostEvent(req):
    return render(req, 'AddEvent.html')