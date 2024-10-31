# forms.py
from django import forms
from .models import Reports, Trails

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['trail', 'report']  # Fields for groomers to fill out

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trail'].queryset = self.fields['trail'].queryset.order_by('trailName')

class TrailForm(forms.ModelForm):
    class Meta:
        model = Trails
        fields = ['trailName', 'location', 'rating']  # Fields for creating a new trail

class ReportApprovalForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['approvalStatus']  # Only include the approval status field
