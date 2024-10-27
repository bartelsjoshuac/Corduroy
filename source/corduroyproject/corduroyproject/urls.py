from django.contrib import admin
from django.urls import path

### Homepage
from corduroyserver.views import index

# Reports
from corduroyserver.views import ReportsViewSet

#Trails
from corduroyserver.views import TrailsViewSet


from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# API endpoints.  Might want to think about splitting out the API from the webserver, like we did in class, but we never connected the webserver to the API, we only tested with postman, so there's that.....
#  Given I will need to make my own pages, I may need to figure this out eventually

router.register(r'reports', ReportsViewSet, basename='reports')
router.register(r'trails', TrailsViewSet, basename='trails')

from rest_framework.routers import DefaultRouter

#urlpatterns = router.urls

# Gotta be a nicer way to work this back in....
# admin is the defaulkt Django admin
# groomers is self explantory
# reportadmin, will be the trail approvers

# The normal Django admin
adminpattern = [
    
    path('admin/', admin.site.urls),
]

urlpatterns = router.urls + adminpattern

urlpatterns = [
    path('', index, name='index'),  # 
]


