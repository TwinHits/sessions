from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Campaign, Session, Character, Note 
from .forms import CampaignForm

# Create your views here.

def sessions_home(request):
    """Returns home page of Sessions"""       
    campaigns = Campaign.objects.all()
    return render(request, "sessions/home.html", {"campaigns": campaigns})

def campaign_detail(request, pk):
    """Returns detail view of a campaign. This campaign is now the active campaign"""
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, "sessions/campaign_detail.html", {"campaign": campaign})

def campaign_new(request):
    """Sets up form for creating a new campaign"""
    if request.method=="POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.create_date = timezone.now()
            campaign.save()
            return redirect("ttgsessions.views.campaign_detail", pk=campaign.pk)
    else:
        form = CampaignForm()
    return render(request, "sessions/campaign_new.html", {"form": form})
