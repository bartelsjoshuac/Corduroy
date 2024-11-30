from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TrailsViewSet,
    ReportsViewSet,
    approved_reports_view,
    homepage_view,  # Add homepage_view for rendering index.html
    groomer_report_view,
    admin_trails_view,
    admin_approval_view
)

# Weather
from .views import get_weather

# Set up a router for the API viewsets
router = DefaultRouter()
router.register(r'trails', TrailsViewSet)
router.register(r'reports', ReportsViewSet)

# Define URL patterns
urlpatterns = [
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Homepage view.  This was needed to render a page with Alpine on / vs /index.html only as it was spitting out JSON page instead of using the
    path('', homepage_view, name='homepage'),  

    # API endpoint for approved reports
    path('approved-reports/', approved_reports_view, name='approved_reports'),  # JSON API endpoint for reports

    # Groomer admin view
    path('groomer-report/add/', groomer_report_view, name='groomer_report_page'),

    # Admin trail management view
    path('admin-trails/', admin_trails_view, name='admin_trails'),

    # Admin approval view
    path('admin-approval/', admin_approval_view, name='admin_approval'),

    # Weather integration - This will generate a 500 server error without the API key configured.
    path('get-weather/', get_weather, name='get_weather'),

    # API viewsets - not used
    path('api/', include(router.urls)),
]
