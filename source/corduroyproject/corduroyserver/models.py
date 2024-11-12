from django.db import models

class Trails(models.Model):
    # Choices for trails.  I supppse there should be a locations admin page, but really these would never change
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

# Table for reports
class Reports(models.Model):
    # As noted in other comment Boolean's have strange processing in Django when you use CSS, they can flip
    approvalStatus = models.BooleanField(default=False)  
    date = models.DateField(auto_now_add=True)  
    groomer = models.CharField(max_length=100)  
    # If a trail is deleted, all reports will be deleted for that trail to maintain integrity
    trail = models.ForeignKey(Trails, related_name='reports', on_delete=models.CASCADE)  
    report = models.TextField()  
    # Don't get the date form the form
    def __str__(self):
        return f'Report for {self.trail.trailName} on {self.date}'
 