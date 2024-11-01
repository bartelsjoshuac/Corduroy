from django import forms
from .models import Reports, Trails

# Groomer and trail list form
# I thnk I should split this so that add reports does not use the same view as displaying them????
class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['trail', 'report']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trail'].queryset = self.fields['trail'].queryset.order_by('trailName')

# Trails admin form
# I need to find a way to set the rating to a default since I can't in the template now
class TrailForm(forms.ModelForm):
    class Meta:
        model = Trails
        fields = ['trailName', 'location', 'rating']  

# Admin admin form for approvals
class ReportApprovalForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['approvalStatus']  
