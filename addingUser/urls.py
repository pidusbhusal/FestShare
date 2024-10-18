from django.urls import path
from . import views

urlpatterns = [
    path('Login', views.Login),
    path('Logout/', views.LogOut),
    path('SignUp', views.RegisterUser),
    path('', views.Home),
    
]