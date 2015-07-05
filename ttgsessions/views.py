from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType

from .models import Campaign, Session, Character, Note 
from .forms import CampaignForm

# Create your views here.

def sessions_home(request):
    """Returns home page of Sessions"""       
    campaigns = Campaign.objects.all()
    return render(request, "sessions/home.html", {"campaigns": campaigns})

def campaign_detail(request, c):
    """Returns detail view of a campaign. This campaign is now the active campaign"""
    campaign = get_object_or_404(Campaign, pk=c)
    sessions = Session.objects.filter(campaign=c)
    notes = campaign.campaign_notes.all()
    return render(request, "sessions/campaign_detail.html", {"campaign": campaign, "sessions": sessions, "notes": notes})

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

def session_detail(request, c, s):
    """From a campaign pk and a session pk, return details of a sesson"""
    campaign = Campaign.objects.get(pk=c) 
    session = Session.objects.get(pk=s)
    notes = session.sessions_notes.all()
    return render(request, "sessions/session_detail.html", {"campaign": campaign, "sessions":session, "notes":notes})
