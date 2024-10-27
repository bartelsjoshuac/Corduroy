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

# My stuff
from .models import Reports
from .models import Trails 
from corduroyserver.serializers import ReportsSerializer
from corduroyserver.serializers import TrailsSerializer

# Reports
# Not that groomers and admins will use the same view.  Groomers will not have access to the approvalStatus flag.  Not sure I can do that securely, but we will find out.  Otherwise, I guess I just make a copy of this view for them
# Sloppy, I dunno

class ReportsViewSet(viewsets.ModelViewSet):
    serializer_class = ReportsSerializer
    queryset = Reports.objects.all()
    
# List all reports, will be used on public page
    def list(self, request):
        queryset = Reports.objects.all()
        serializer = ReportsSerializer(queryset, many=True)
        return Response(serializer.data)
    
# Create a new report, will be used on groomer page
    def create(self, request):    
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Retrive a single trail (might not need this)
    def retrieve(self, request, pk=None):
        queryset = Reports.objects.all()
        reports = get_object_or_404(queryset, pk=pk)
        serializer = ReportSerializer(reports)
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

# Trails
class TrailsViewSet(viewsets.ModelViewSet):
    serializer_class = TrailsSerializer
    queryset = Trails.objects.all()
    
# List all Trails, will be used on public page
    def list(self, request):
        queryset = Trails.objects.all()
        serializer = TrailsSerializer(queryset, many=True)
        return Response(serializer.data)
    
# Create a new trail, will be used on groomer page
    def create(self, request):    
        serializer = TrailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
def home(request):
    return render(request, 'index.html')