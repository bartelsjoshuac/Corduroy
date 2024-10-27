from django.contrib import admin
from django.urls import path

### Pages
from corduroyserver.views import index
from corduroyserver.views import groomers
from corduroyserver.views import reportsadmin
from corduroyserver.views import trailsadmin

# Reports
from corduroyserver.views import ReportsViewSet


# Trails
from corduroyserver.views import TrailsViewSet

# The router stuff from one of the exercises
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'reports', ReportsViewSet, basename='reports')


router.register(r'trails', TrailsViewSet, basename='trails')


from rest_framework.routers import DefaultRouter

###########  This is is good for admin and 
# The normal Django admin, this is how I was combing admin with my router
adminpattern = [
    
    path('admin/', admin.site.urls),
]

indexpattern = [
    
    path('', admin.site.urls),
]

# This combines my admin pattern (which must be an object???? with the router and it works)
urlpatterns = router.urls + adminpattern

# This overwrites it, and leaves me with only my admin and my homepage and I can't get my router in there.
urlpatterns = [
    path('', index, name='index'),
    path('groomers.html', groomers, name='groomers'),
    path('reportsadmin.html', reportsadmin, name='reportsadmin'),
    path('trailsadmin.html', trailsadmin, name='trailsadmin'),
    path('admin/', admin.site.urls),  
]

# Wow, this now works and is so sloppy, but given the time I spent on it....... Not about to mess with it ever.
urlpatterns += router.urls
