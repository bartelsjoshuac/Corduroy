from rest_framework import serializers
from .models import Trails, Reports

class TrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trails
        fields = ['id', 'trailName', 'location', 'rating']

class ReportsSerializer(serializers.ModelSerializer):

    # Fields for computed trail details (output only)
    trail_name = serializers.CharField(source='trail.trailName', read_only=True)
    location = serializers.CharField(source='trail.location', read_only=True)
    
    # Use the TrailsSerializer if you want to include nested trail data
    trail_details = TrailsSerializer(source='trail', read_only=True)

    # This is used for the homepage for un-authenticated users
    class Meta:
        model = Reports
        fields = [
            'id', 'approvalStatus', 'date', 'groomer', 'trail', 'trail_name', 'location',
            'trail_details', 'report'
        ]
