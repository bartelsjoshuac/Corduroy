from django.contrib import admin
from .models import Reports

class ReportsAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('approvalStatus', 'date','groomer', 'trailName', 'report')
    
    # Add search functionality for specific fields
    search_fields = ('approvalStatus', 'date','groomer', 'trailName', 'report')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('approvalStatus', 'date','groomer', 'trailName', 'report')

    # Define which fields can be clicked to view the details page
    list_display_links = ('trailName',)

    # Define how fields are displayed when editing a Report instance
    fields = ('approvalStatus', 'date','groomer', 'trailName', 'report')

# Register the model and admin class
admin.site.register(Reports, ReportsAdmin)
