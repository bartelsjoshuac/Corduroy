from rest_framework import serializers
from .models import Reports
from .models import Trails

# Added ID, but it is not working, except there is indeed an ID wthat gets populate 

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id','approvalStatus', 'date', 'groomer', 'trailName', 'report']

class ReportsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['id','approvalStatus', 'date', 'groomer', 'trailName', 'report']

class TrailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trails
        fields = ['id','trailName', 'location', 'rating']

