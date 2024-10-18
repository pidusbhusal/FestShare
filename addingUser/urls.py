from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login),
    path('Logout/', views.LogOut),
    path('greetUser/', views.CreateNewUser),
    path('SignUp/', views.SignUp),
    path('', views.Home),
    
]