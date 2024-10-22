
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('addingUser.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('money_tracker.urls')),
    path('events/', include('events.urls'))
    
   
]
