from django.db import models

# To constrain trail rating 1-10
from django.core.validators import MaxValueValidator, MinValueValidator

# To constrain trail locations
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Table of Reports   
class Reports(models.Model):
    # This default of false is need for when Groomers enter a report because they can not update that.
    approvalStatus = models.BooleanField(default=False)
    date = models.DateField()
    groomer = models.CharField(max_length=100)
    # Need some admin flows for this because we can't change code just to add new trails
    #TRAILS = ( 
    #('Shrine Pass', 'Shrine Pass'), 
    #('Owl Creek Road', 'Owl Creek Road'), 
    #) 
    #trailName = models.CharField(max_length=100,choices=TRAILS)
    trailName = models.CharField(max_length=100)
    report = models.CharField(max_length=1000)

    def __str__(self):
        return self.trailName



# Table of Trails
class Trails(models.Model):
    trailName = models.CharField(max_length=100)
    # Need some admin flows for this because we can't change code just to add new locations
    LOCATIONS = ( 
    ('Front Range', 'Front Range'), 
    ('San Juans', 'San Juans'), 
    ) 
    location = models.CharField(max_length=100, choices=LOCATIONS)  
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
   
    def __str__(self):
        return self.trailName
