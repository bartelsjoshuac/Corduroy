from django.contrib import admin
from django.urls import path

# Reports
from corduroyserver.views import ReportsViewSet

#Trails
from corduroyserver.views import TrailsViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'reports', ReportsViewSet, basename='reports')
router.register(r'trails', Trails
                ViewSet, basename='trails')

from rest_framework.routers import DefaultRouter

#urlpatterns = router.urls

# Gotta be a nicer way to work this back in....
adminpattern = [
    
    path('admin/', admin.site.urls),
]

urlpatterns = router.urls + adminpattern
