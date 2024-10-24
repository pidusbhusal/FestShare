from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('BeSponser', views.BeSponser, name="form to be sponser"),
    path('AddSponser', views.AddSponser, name="AddSponser"),
 

]
