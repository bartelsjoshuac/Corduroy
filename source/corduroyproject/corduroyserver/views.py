from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from .models import Trails, Reports
from .serializers import TrailsSerializer, ReportsSerializer
from .forms import ReportForm, TrailForm, ReportApprovalForm

# API viewsets for Trails and Reports models.
class TrailsViewSet(viewsets.ModelViewSet):
    queryset = Trails.objects.all()
    serializer_class = TrailsSerializer

class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

# Homepage view to display approved reports
def approved_reports_view(request):
    # Only display reports to the public that have been approved.  Not doing this in the template now
    # For now display all reports, even multiple per trail for historical perspective but need to rethink this longer term as we can't have 100 reports for one trail show up,  Maybe max of 5???
    approved_reports = Reports.objects.filter(approvalStatus=True).order_by('-date')
    return render(request, 'index.html', {'approved_reports': approved_reports})

@login_required
def groomer_report_view(request):
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

    # Group trails by location for the select list
    trails_by_location = {}
    for trail in Trails.objects.all():
        location = trail.location
        if location not in trails_by_location:
            trails_by_location[location] = []
        trails_by_location[location].append({'id': trail.id, 'name': trail.trailName})

    return render(request, 'groomer_report.html', {
        'form': form,
        'trails_by_location': trails_by_location
    })

# Admin view for trails
@login_required
def admin_trails_view(request):
    # Ensure the user is in the admins group
    if not request.user.groups.filter(name="admins").exists():
        return render(request, 'not_authorized.html') 

    if request.method == 'POST':
        if 'delete' in request.POST: 
            trail_id = request.POST.get('delete')
            trail = Trails.objects.filter(id=trail_id).first()
            if trail:
                trail.delete()
            # Ensure form is initialized after deletion to avoid UnboundLocalError
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


# Admin view for changing approval status of reports, restricted to admins group
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
    else:
        reports = Reports.objects.all()
        form = ReportApprovalForm()

    return render(request, 'admin_approval.html', {'form': form, 'reports': reports})
