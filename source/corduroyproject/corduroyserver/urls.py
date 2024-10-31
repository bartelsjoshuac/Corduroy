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

# Set up a router for the API viewsets
router = DefaultRouter()
router.register(r'trails', TrailsViewSet)
router.register(r'reports', ReportsViewSet)

# Define URL patterns
urlpatterns = [
    path('', approved_reports_view, name='homepage'),  # Homepage displaying approved reports
    path('groomer-report/add/', groomer_report_view, name='groomer_report_page'),  # Groomer report form page
    path('admin-trails/', admin_trails_view, name='admin_trails'),  # Admin trail management page
    path('admin-approval/', admin_approval_view, name='admin_approval'),  # Admin report approval management page
    path('api/', include(router.urls)),  # API endpoints for Trails and Reports
]

