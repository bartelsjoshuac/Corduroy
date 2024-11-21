from rest_framework import serializers
from .models import Trails, Reports

class TrailsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Trails model, used for nested and standalone trail data.
    """
    class Meta:
        model = Trails
        fields = ['id', 'trailName', 'location', 'rating']

class ReportsSerializer(serializers.ModelSerializer):
    """
    Serializer for the Reports model. Includes nested trail details.
    """
    # Fields for computed trail details (output only)
    trail_name = serializers.CharField(source='trail.trailName', read_only=True)
    location = serializers.CharField(source='trail.location', read_only=True)
    # Use the TrailsSerializer if you want to include nested trail data
    trail_details = TrailsSerializer(source='trail', read_only=True)

    class Meta:
        model = Reports
        fields = [
            'id', 'approvalStatus', 'date', 'groomer', 'trail', 'trail_name', 'location',
            'trail_details', 'report'
        ]
