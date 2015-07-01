from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Campaign, Session, Character, Note 

# Create your views here.

def sessions_home(request):
    """Returns home page of Sessions"""       
    campaigns = Campaign.objects.all()
    return render(request, "sessions/home.html", {"campaigns": campaigns})

def campaign_detail(request, pk):
    """Returns detail view of a campaign. This campaign is now the active campaign"""
    campaign = get_object_or_404(Campaign, pk=pk)
    #active_campaign = campaign
    return render(request, "sessions/campaign_detail.html", {"campaign": campaign})
