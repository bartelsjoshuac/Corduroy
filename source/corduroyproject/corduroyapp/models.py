from django.db import models

# To constrain trail rating 1-10
from django.core.validators import MaxValueValidator, MinValueValidator

# To constrain trail locations
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Table of Trails
class Trails(models.Model):
    trailname = models.CharField(max_length=100)
    LOCATIONS = ( 
    ('Front Range', 'Front Range'), 
    ('San Juans', 'San Juans'), 
    ) 
    location = models.CharField(max_length=100, choices=LOCATIONS)  
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    
    def __str__(self):
        return self.name

#Table of Reports   
class Reports(models.Model):
    approvalStatus = models.BooleanField()
    date = models.DateField()
    groomer = models.CharField(max_length=100)
    # In the future we would have a trail admin view for admins to main trail name, but we are only letting groomers pic for now
    TRAILS = ( 
    ('Shrine Pass', 'Shrine Pass'), 
    ('Owl Creek Road', 'Owl Creek Road'), 
    ) 
    trailName = models.CharField(max_length=100,choices=TRAILS)
    report = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
