from django.db import models

# To constrain trail rating 1-10
from django.core.validators import MaxValueValidator, MinValueValidator

# To constrain trail locations
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Table of Trails
class Trails(models.Model):
    trailName = models.CharField(max_length=100)
    # If I make a trails admin, then this can be removed.
    LOCATIONS = ( 
    ('Front Range', 'Front Range'), 
    ('San Juans', 'San Juans'), 
    ('Grand Mesa', 'Grand Mesa'), 
    ('Grand Lake', 'Grand Lake'),
    ('Other', 'Other'),
    ) 
    location = models.CharField(max_length=100, choices=LOCATIONS)  
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
   
    def __str__(self):
        return self.trailName

#Table of Reports   
class Reports(models.Model):
    # This default of false is need for when Groomers enter a report because they can not update that. But this does not work, so I am going to go insecure and put it in the form.
    approvalStatus = models.BooleanField(default=True)
    date = models.DateField()
    groomer = models.CharField(max_length=100)
    trailName = models.CharField(max_length=100)
    
    # Fixed the model based on feedback from exercise but this is not working, which again seems to be a postgres vs. sqlite thing
    # trailName = models.ForeignKey(Trails, on_delete=models.CASCADE)
    # I must have tried 20 different ways to do this, trashed my database.... spent hours on it and gave up.
    
    report = models.CharField(max_length=1000)

    def __str__(self):
        return self.trailName#




