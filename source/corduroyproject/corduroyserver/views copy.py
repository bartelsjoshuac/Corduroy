from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
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

    @action(detail=True, methods=['patch'])
    def update_approval(self, request, pk=None):

        # Updates the approval status only for a report
        report = self.get_object()
        approval_status = request.data.get('approvalStatus')
        if approval_status is not None:
            report.approvalStatus = approval_status
            report.save()
            return Response({'status': 'Approval status updated'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        # Handle the new groomer reports with the auto date and authenticated user as the groomer that submitted the report
        data = request.data.copy()
        if 'trail' not in data or 'report' not in data:
            return Response({'error': 'Missing required fields: trail or report'}, status=status.HTTP_400_BAD_REQUEST)

        # Add additional fields
        data['groomer'] = request.user.username  # Set groomer to logged-in user
        data['approvalStatus'] = False  # Default approval status
        data['date'] = timezone.now().date()  # Current date, would be nice to add time with the date?

        # Serialize and save
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# API endpoint to serve approved reports for Alpine in JSON vs HTML
def approved_reports_view(request):
    if request.method == 'GET':
        reports = Reports.objects.filter(approvalStatus=True).select_related('trail').order_by('-date')
        serializer = ReportsSerializer(reports, many=True)
        return JsonResponse(serializer.data, safe=False)


# Homepage view for server-side rendering in Alpine
def homepage_view(request):
    approved_reports = Reports.objects.filter(approvalStatus=True).order_by('-date')
    return render(request, 'index.html', {'approved_reports': approved_reports})

@login_required
def groomer_report_view(request):
    """
    View for groomers to enter reports.
    """
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
        else:
            return JsonResponse({'error': form.errors}, status=400)

    trails_by_location = {}
    trails = Trails.objects.all()

    if not trails.exists():
        return render(request, 'no_trails.html')

    for trail in trails:
        location = trail.location
        if location not in trails_by_location:
            trails_by_location[location] = []
        trails_by_location[location].append({'id': trail.id, 'name': trail.trailName})

    return render(request, 'groomer_report.html', {
        'trails_by_location': trails_by_location,
    })


@login_required
def admin_trails_view(request):
    """
    Admin view for managing trails.
    """
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

    return render(request, 'admin_approval.html', {
        'form': form,
        'reports': reports,
    })


# This view is inteded for an Ajax call so the new reports will appear in the homepage dynamically
def check_new_reports(request):
    has_new_reports = Report.objects.filter(approval_status=True).exists()
    return JsonResponse({'new_reports': has_new_reports})


# Again there is some redundancy in here to clean up, leftover from the dogapi days and Django


