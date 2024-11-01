# These are the base project urls like the admin, we will add ours in the server
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('corduroyserver.urls')),  
]



