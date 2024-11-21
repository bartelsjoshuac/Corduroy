from rest_framework import serializers
from .models import Trails, Reports

class TrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trails
        fields = ['id', 'trailName', 'location', 'rating']

class ReportsSerializer(serializers.ModelSerializer):
    # Include trail details from the related Trails model
    trail_name = serializers.CharField(source='trail.trailName')
    location = serializers.CharField(source='trail.location')

    class Meta:
        model = Reports
        fields = ['id', 'approvalStatus', 'date', 'groomer', 'trail', 'trail_name', 'location', 'report']
