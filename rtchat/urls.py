from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
 
    path('Chat',views.chat_view,name='Chat'),
    
]
