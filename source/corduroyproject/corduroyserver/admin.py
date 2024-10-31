from django.contrib import admin
from .models import Trails, Reports

class ReportsInline(admin.TabularInline):
    model = Reports
    extra = 1  

@admin.register(Trails)
class TrailsAdmin(admin.ModelAdmin):
    list_display = ('trailName', 'location', 'rating')  
    search_fields = ('trailName', 'location')  
    inlines = [ReportsInline]  

@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('groomer', 'trail', 'date', 'approvalStatus')  
    list_filter = ('approvalStatus', 'trail')  
    search_fields = ('groomer', 'trail__trailName')  
    list_editable = ('approvalStatus',)  
