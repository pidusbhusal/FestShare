from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Onboarding, name="Onboarding"),
    path('Home', views.Home),
    path('Chat/',views.Chat,name='Chat'),
    path('PostEvent/',views.PostEvent,name='PostEvent')
]