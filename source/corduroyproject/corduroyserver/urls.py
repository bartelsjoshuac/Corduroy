from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrailsViewSet,
    ReportsViewSet,
    approved_reports_view,
    groomer_report_view,
    admin_trails_view,
    admin_approval_view
)
from django.urls import path


# Set up a router for the API viewsets
router = DefaultRouter()
router.register(r'trails', TrailsViewSet)
router.register(r'reports', ReportsViewSet)

# Define URL patterns
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', approved_reports_view, name='homepage'),  
    path('groomer-report/add/', groomer_report_view, name='groomer_report_page'),  
    path('admin-trails/', admin_trails_view, name='admin_trails'),  
    path('admin-approval/', admin_approval_view, name='admin_approval'),  
    path('api/', include(router.urls)),  
]

