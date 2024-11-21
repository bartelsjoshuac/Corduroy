from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from django.http import JsonResponse
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


# API endpoint to serve approved reports for dynamic front-end
def approved_reports_view(request):
    """
    Returns JSON response with approved reports for dynamic rendering.
    """
    if request.method == 'GET':
        # Filter approved reports and fetch related trail data
        reports = Reports.objects.filter(approvalStatus=True).select_related('trail').order_by('-date')
        # Serialize data using ReportsSerializer
        serializer = ReportsSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)


# Homepage view (only needed if you still want to use server-side rendering)
def homepage_view(request):
    approved_reports = Reports.objects.filter(approvalStatus=True).order_by('-date')
    return render(request, 'index.html', {'approved_reports': approved_reports})


@login_required
def groomer_report_view(request):
    """
    View for groomers to enter reports.
    """
    # Check if the user is in the "groomers" group
    if not request.user.groups.filter(name="groomers").exists():
        return render(request, 'not_authorized.html')

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            # Set the groomer to the authenticated user
            report.groomer = request.user.username
            # Set the current date
            report.date = timezone.now().date()
            report.save()
            return redirect('homepage')
    else:
        form = ReportForm()

    # Group trails by location for the select list
    trails_by_location = {}
    trails = Trails.objects.all()

    if not trails.exists():
        # If there are no trails, handle the case gracefully
        return render(request, 'no_trails.html')

    for trail in trails:
        location = trail.location
        if location not in trails_by_location:
            trails_by_location[location] = []
        trails_by_location[location].append({'id': trail.id, 'name': trail.trailName})

    # Pass the form and trails data to the template
    context = {
        'form': form,
        'trails_by_location': trails_by_location,
    }

    return render(request, 'groomer_report.html', context)


@login_required
def admin_trails_view(request):
    """
    Admin view for managing trails.
    """
    # Ensure the user is in the admins group
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')

    if request.method == 'POST':
        if 'delete' in request.POST:
            trail_id = request.POST.get('delete')
            trail = Trails.objects.filter(id=trail_id).first()
            if trail:
                trail.delete()
            form = TrailForm()
        else:
            form = TrailForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_trails')
    else:
        form = TrailForm()

    trails = Trails.objects.all()
    return render(request, 'admin_trails.html', {'form': form, 'trails': trails})


@login_required
def admin_approval_view(request):
    """
    Admin view for approving or rejecting reports.
    """
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')

    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        report = get_object_or_404(Reports, id=report_id)
        form = ReportApprovalForm(request.POST, instance=report)

        if form.is_valid():
            form.save
