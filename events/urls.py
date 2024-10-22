from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Onboarding, name="Onboarding"),
    path('', views.Home, name = "Home")

    
]
