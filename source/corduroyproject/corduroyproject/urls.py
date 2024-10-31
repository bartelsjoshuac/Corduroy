# corduroyproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('corduroyserver.urls')),  # Include URLs from the corduroyserver app
]



