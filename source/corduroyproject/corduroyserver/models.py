from django.db import models

from django.db import models

class Trails(models.Model):
    # Location choices for trails
    LOCATIONS = (
        ('Front Range', 'Front Range'), 
        ('San Juans', 'San Juans'), 
        ('Grand Mesa', 'Grand Mesa'), 
        ('Grand Lake', 'Grand Lake'),
        ('Other', 'Other'),
    )
    trailName = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=LOCATIONS)  # Restricted to predefined choices
    rating = models.IntegerField()

    def __str__(self):
        return self.trailName



class Reports(models.Model):
    approvalStatus = models.BooleanField(default=False)  # Indicates if the report is approved
    date = models.DateField(auto_now_add=True)  # Automatically set the field to now when created
    groomer = models.CharField(max_length=100)  # Name of the groomer
    trail = models.ForeignKey(Trails, related_name='reports', on_delete=models.CASCADE)  # Related trail
    report = models.TextField()  # Detailed report content

    def __str__(self):
        return f'Report for {self.trail.trailName} on {self.date}'
