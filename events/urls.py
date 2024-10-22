from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Onboarding, name="Onboarding"),
    path('Home', views.Home),
    path('Chat',views.Chat,name='Chat'),
    path('AddEvent', views.AddEvent, name = "Event Post Form"),
    path('joinEvent', views.joinEvent, name = "Joining The Event"), 
    path('ProceedToCheckout', views.ProceedToCheckout, name = "Joining Event Checkout")
]
