from django.db import models
from django.db import models

class Trails(models.Model):
    # Table choices for trails
    LOCATIONS = (
        ('Front Range', 'Front Range'), 
        ('San Juans', 'San Juans'), 
        ('Grand Mesa', 'Grand Mesa'), 
        ('Grand Lake', 'Grand Lake'),
        ('Other', 'Other'),
    )
    trailName = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=LOCATIONS)  
    rating = models.IntegerField()

    def __str__(self):
        return self.trailName

# Table choices for reports
class Reports(models.Model):
    approvalStatus = models.BooleanField(default=False)  
    date = models.DateField(auto_now_add=True)  
    groomer = models.CharField(max_length=100)  
    # If a trail is deleted, all reports will be deleted for that trail
    trail = models.ForeignKey(Trails, related_name='reports', on_delete=models.CASCADE)  
    report = models.TextField()  

    def __str__(self):
        return f'Report for {self.trail.trailName} on {self.date}'
