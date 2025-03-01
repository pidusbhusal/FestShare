
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('addingUser.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('events.urls')),
    path('', include('rtchat.urls')), 
    path('', include('sponsers.urls'))

    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)