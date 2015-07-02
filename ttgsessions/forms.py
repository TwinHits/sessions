from django import forms
from .models import Campaign 

class CampaignForm(forms.ModelForm):
    """Form to create a new campaign. Takes name, start date, system"""
    class Meta:
        model = Campaign
        fields = ("name", "start_date")
        #system
