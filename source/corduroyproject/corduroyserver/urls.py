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
    # This registration is some sort of Django default
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Homepage view
    path('', approved_reports_view, name='homepage'),  
    # Groomer admin view
    path('groomer-report/add/', groomer_report_view, name='groomer_report_page'),  
    # Admin trail admin view
    path('admin-trails/', admin_trails_view, name='admin_trails'),  
    # Admin approval view
    path('admin-approval/', admin_approval_view, name='admin_approval'),  
    
    #path('api/', include(router.urls)),  
]

