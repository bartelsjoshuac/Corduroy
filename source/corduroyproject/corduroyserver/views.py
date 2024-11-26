from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import requests

from .models import Trails, Reports
from .serializers import TrailsSerializer, ReportsSerializer
from .forms import ReportForm, TrailForm, ReportApprovalForm


# API viewsets for Trails and Reports models
class TrailsViewSet(viewsets.ModelViewSet):
    queryset = Trails.objects.all()
    serializer_class = TrailsSerializer


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.select_related('trail').all()
    serializer_class = ReportsSerializer

    @action(detail=True, methods=['patch'])
    def update_approval(self, request, pk=None):
        report = self.get_object()
        approval_status = request.data.get('approvalStatus')
        if approval_status is not None:
            report.approvalStatus = approval_status
            report.save()
            return Response({'status': 'Approval status updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if 'trail' not in data or 'report' not in data:
            return Response({'error': 'Missing required fields: trail or report'}, status=status.HTTP_400_BAD_REQUEST)

        data['groomer'] = request.user.username
        data['approvalStatus'] = False
        data['date'] = timezone.now().date()

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# View for fetching approved reports
def approved_reports_view(request):
    reports = Reports.objects.filter(approvalStatus=True).select_related('trail').order_by('-date')
    serializer = ReportsSerializer(reports, many=True)
    return JsonResponse(serializer.data, safe=False)


# Homepage view
def homepage_view(request):
    approved_reports = Reports.objects.filter(approvalStatus=True).order_by('-date')
    return render(request, 'index.html', {'approved_reports': approved_reports})


@login_required
def groomer_report_view(request):
    if not request.user.groups.filter(name="groomers").exists():
        return render(request, 'not_authorized.html')

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.groomer = request.user.username
            report.date = timezone.now().date()
            report.save()
            return JsonResponse({'message': 'Report submitted successfully!'}, status=201)
        return JsonResponse({'error': form.errors}, status=400)

    trails_by_location = {}
    trails = Trails.objects.all()

    if not trails.exists():
        return render(request, 'no_trails.html')

    for trail in trails:
        location = trail.location
        trails_by_location.setdefault(location, []).append({'id': trail.id, 'name': trail.trailName})

    return render(request, 'groomer_report.html', {'trails_by_location': trails_by_location})


@login_required
def admin_trails_view(request):
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')

    form = TrailForm(request.POST or None)
    if request.method == 'POST':
        if 'delete' in request.POST:
            trail = Trails.objects.filter(id=request.POST.get('delete')).first()
            if trail:
                trail.delete()
        elif form.is_valid():
            form.save()
            return redirect('admin_trails')

    trails = Trails.objects.all()
    return render(request, 'admin_trails.html', {'form': form, 'trails': trails})


@login_required
def admin_approval_view(request):
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')

    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        report = get_object_or_404(Reports, id=report_id)
        form = ReportApprovalForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('admin_approval')

    reports = Reports.objects.all()
    form = ReportApprovalForm()
    return render(request, 'admin_approval.html', {'form': form, 'reports': reports})


# Ajax view for new reports
def check_new_reports(request):
    has_new_reports = Reports.objects.filter(approvalStatus=True).exists()
    return JsonResponse({'new_reports': has_new_reports})


# Weather API integration - Make sure API Key is in settings.py, but otherwise this fails gracefully
import requests
from django.http import JsonResponse
from django.conf import settings

def get_weather(request):
    city = "Leadville"  # Central high alpine location
    state = "CO"
    country = "US"
    api_key = settings.WEATHER_API_KEY
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=imperial"
    # Not working
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{state},{country}&appid={api_key}&units=imperial"

    # Fetch current weather
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        return JsonResponse({'error': 'Could not fetch current weather data'}, status=500)

    # Fetch weather forecast
    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        return JsonResponse({'error': 'Could not fetch weather forecast data'}, status=500)

    weather_data = weather_response.json()
    forecast_data = forecast_response.json()

    # Extract required data
    current_weather = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'], 
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
    }

    forecast = [
        {
            'date': item['dt_txt'],
            'temperature': item['main']['temp'], 
            'description': item['weather'][0]['description'],
            'icon': item['weather'][0]['icon'],
        }
        for item in forecast_data['list'][:3]  
    ]

    return JsonResponse({'current': current_weather, 'forecast': forecast})


   

