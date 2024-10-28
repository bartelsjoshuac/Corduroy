# Standard stuff I need, or I think I need
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets

### Stuff I added for authentcation
### For authentication
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect

# My stuff
from .models import Reports
from .models import Trails 

from corduroyserver.serializers import ReportsSerializer
from corduroyserver.serializers import ReportsAdminSerializer
from corduroyserver.serializers import TrailsSerializer

#### Require auth for groomers and report admins
class GroupRequiredMixin(UserPassesTestMixin):
    group_name = None  

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(name=self.group_name).exists()

    def handle_no_permission(self):
        return redirect('/admin/login/')  


########################### Reports #######################################
class ReportsViewSet(viewsets.ModelViewSet):
    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()
    
# List all reports, will be used on public page
    def list(self, request):
        queryset = Reports.objects.all()
        serializer = ReportsSerializer(queryset, many=True)
        
        context = {
            'reports' : serializer.data
        }
        # Added context here
        return render(request, 'reports.html', context)
        return Response(serializer.data)

# Create a new report, will be used on groomer page
    def create(self, request):    
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'success.html')
            return Response(serializer.data)
        return Response(serializer.errors)

# Retrive a single report (might not need this)
    def retrieve(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(reports)
        return Response(serializer.data)
    
# Update a report, which will be needed by admin to approve or modify report
    def update(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(reports, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# Delete a report which we will not need now
    def destroy(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsSerializer(reports)
        reports.delete()
        return Response({'Success': 'This deleted a report.'}, status=status.HTTP_200_OK)

########################### ReportsAdmin #######################################

class ReportsAdminViewSet(viewsets.ModelViewSet):
####
### With group check but I need a login page, and to serperate this into two view, or use attribute security
#class ReportsAdminViewSet(GroupRequiredMixin, viewsets.ModelViewSet):
####

    group_name = 'ReportsAdmin'  or "Groomers"
    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()
    
# List all reports, will be used on public page
    def list(self, request):
        queryset = Reports.objects.all()
        serializer = ReportsAdminSerializer(queryset, many=True)
        
        context = {
            'reports' : serializer.data
        }
        return render(request, 'reportsadmin.html', context)
        return Response(serializer.data)

# Create a new report, will be used on groomer page
    def create(self, request):    
        serializer = ReportsAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'success.html')
            return Response(serializer.data)
        return Response(serializer.errors)

# Retrive a single report (might not need this)
    def retrieve(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsAdminSerializer(reports)
        return Response(serializer.data)
    
# Update a report, which will be needed by admin to approve or modify report
    def update(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsAdminSerializer(reports, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# Delete a report which we will not need now
    def destroy(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportsAdminSerializer(reports)
        reports.delete()
        return Response({'Success': 'This deleted a report.'}, status=status.HTTP_200_OK)

########################### Trails #######################################
#class TrailsViewSet(GroupRequiredMixin, viewsets.ModelViewSet):
####
    # No Groomers on the trails page
    #group_name = 'ReportsAdmin'

class TrailsViewSet(viewsets.ModelViewSet):
    serializer_class = TrailsSerializer
    queryset = Trails.objects.all()
    
# List all Trails, will be used on public page
    def list(self, request):
        queryset = Trails.objects.all()
        serializer = TrailsSerializer(queryset, many=True)
        context = {
            'trails' : serializer.data
        }
        return render(request, 'trails.html',context)
        return Response(serializer.data)
        
    
# Create a new trail, will be used on groomer page
    def create(self, request):    
        serializer = TrailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'success.html')
            return Response(serializer.data)
        return Response(serializer.errors)

# Retrive a single trail (might not need this)
    def retrieve(self, request, pk=None):
        queryset = Trails.objects.all()
        Trails = get_object_or_404(queryset, pk=pk)
        serializer = Trailserializer(Trails)
        return Response(serializer.data)
    
# Update a trail, which will be needed by admin to approve or modify trail
    def update(self, request, pk=None):
        queryset = Trails.objects.all()
        Trails = get_object_or_404(queryset, pk=pk)
        serializer = TrailsSerializer(Trails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# Delete a trail which we will not need now
    def destroy(self, request, pk=None):
        queryset = Trails.objects.all()
        Trails = get_object_or_404(queryset, pk=pk)
        serializer = TrailsSerializer(Trails)
        Trails.delete()
        return Response({'Success': 'This deleted a trail.'}, status=status.HTTP_200_OK)



# Define a home landing page for the app
def index(request):
    return render(request, 'index.html')

# Define a page for groomers
def groomers(request):
    return render(request, 'groomers.html')

# Define a page for reports
def reports(request):
    return render(request, 'reports.html')

# Define a page for reports admins
def reportsadmin(request):
    return render(request, 'reportsadmin.html')

# Define a page for trails admins
def trailsadmin(request):
    return render(request, 'trailsadmin.html')



