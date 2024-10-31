from django.contrib import admin
from .models import Trails, Reports

class ReportsInline(admin.TabularInline):
    model = Reports
    extra = 1  # Number of empty report forms to display

@admin.register(Trails)
class TrailsAdmin(admin.ModelAdmin):
    list_display = ('trailName', 'location', 'rating')  # Fields to display in the list view
    search_fields = ('trailName', 'location')  # Fields to search
    inlines = [ReportsInline]  # Inline reports in the trails admin page

@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('groomer', 'trail', 'date', 'approvalStatus')  # Fields to display in the list view
    list_filter = ('approvalStatus', 'trail')  # Filters to apply on the list view
    search_fields = ('groomer', 'trail__trailName')  # Search fields
    list_editable = ('approvalStatus',)  # Editable fields in list view
