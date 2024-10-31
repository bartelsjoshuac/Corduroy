# serializers.py
from rest_framework import serializers
from .models import Trails, Reports

class TrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trails
        fields = ['id', 'trailName', 'location', 'rating']

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id', 'approvalStatus', 'date', 'groomer', 'trail', 'report']
