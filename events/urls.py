from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Onboarding, name="Onboarding"),
    path('Home', views.Home),
    path('leaveEvent', views.leaveEvent),
    path('AddEvent', views.AddEvent, name = "Event Post Form"),
    path('joinEvent', views.joinEvent, name = "Joining The Event"), 
    path('ProceedToCheckout', views.ProceedToCheckout, name = "Joining Event Checkout"),
    path('YourEvent', views.yourEvent, name = "website for your event."),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),  # Add this line

]
