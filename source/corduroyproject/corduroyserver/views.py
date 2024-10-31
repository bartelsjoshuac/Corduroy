from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from .models import Trails, Reports
from .serializers import TrailsSerializer, ReportsSerializer
from .forms import ReportForm, TrailForm, ReportApprovalForm

# API viewsets for Trails and Reports models
class TrailsViewSet(viewsets.ModelViewSet):
    queryset = Trails.objects.all()
    serializer_class = TrailsSerializer

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

# Homepage view to display approved reports
def approved_reports_view(request):
    # Fetch reports where approvalStatus is True
    approved_reports = Reports.objects.filter(approvalStatus=True).order_by('-date')
    return render(request, 'index.html', {'approved_reports': approved_reports})

# Groomer report form view, restricted to groomers group
@login_required
def groomer_report_view(request):
    # Ensure only members of the 'groomers' group can access this view
    if not request.user.groups.filter(name="groomers").exists():
        return render(request, 'not_authorized.html')  # Access denied page

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.groomer = request.user.username  # Set groomer to the authenticated user
            report.date = timezone.now().date()  # Set the current date
            report.save()
            return redirect('homepage')  # Redirect to homepage after submission
    else:
        form = ReportForm()

    return render(request, 'groomer_report.html', {'form': form})

# Admin view for adding and deleting trails, restricted to admins group
@login_required
def admin_trails_view(request):
    # Ensure the user is in the 'admins' group
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')  # Access denied page

    if request.method == 'POST':
        if 'delete' in request.POST:  # Handle delete action
            trail_id = request.POST.get('delete')
            trail = Trails.objects.filter(id=trail_id).first()
            if trail:
                trail.delete()
        else:  # Handle adding a new trail
            form = TrailForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_trails')
    else:
        form = TrailForm()

    trails = Trails.objects.all()  # List all trails for deletion
    return render(request, 'admin_trails.html', {'form': form, 'trails': trails})

# Admin view for changing approval status of reports, restricted to admins group
@login_required
def admin_approval_view(request):
    # Ensure only members of the 'admins' group can access this view
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html')  # Access denied page

    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        report = get_object_or_404(Reports, id=report_id)
        form = ReportApprovalForm(request.POST, instance=report)
        
        if form.is_valid():
            form.save()
            return redirect('admin_approval')  # Redirect to the same page after submission
    else:
        # Display all reports for selection
        reports = Reports.objects.all()
        form = ReportApprovalForm()

    return render(request, 'admin_approval.html', {'form': form, 'reports': reports})
