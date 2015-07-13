from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import EmptyQuerySet

from .models import Campaign, Session, Character, Note 
from .forms import CampaignForm

# Create your views here.

def sessions_home(request):
    """Returns home page of Sessions"""       
    campaigns = Campaign.objects.all()
    last_session_dates = {} 
    for i in campaigns:
        sesses = Session.objects.filter(campaign=i)
        if sesses:
            last_session_dates[i.pk] = str(sesses.latest("date").date.date())
        else: 
            last_session_dates[i.pk] = "-"
    return render(request, "notes/home.html", {"campaigns": campaigns, "last_session_dates": last_session_dates})

def campaign_detail(request, campaign):
    """Returns detail view of a campaign. This campaign is now the active campaign"""
    campaign = get_object_or_404(Campaign, pk=campaign)
    sessions = Session.objects.filter(campaign=campaign)
    notes = campaign.notes.all()
    characters = Character.objects.filter(campaign=campaign)
    return render(request, "notes/campaign_detail.html", {"campaign": campaign, "sessions": sessions, "notes": notes, "characters": characters})

def campaign_new(request):
    """Sets up form for creating a new campaign"""
    if request.method=="POST":
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.date = timezone.now()
            campaign.save()
            return redirect("notes.views.campaign_detail", campaign=campaign.pk)
    else:
        form = CampaignForm()
    return render(request, "notes/campaign_new.html", {"form": form})

def session_detail(request, campaign, session):
    """From a campaign pk and a session pk, return details of a sesson"""
    campaign = Campaign.objects.get(pk=campaign) 
    session = Session.objects.get(pk=session)
    notes = session.notes.all()
    return render(request, "notes/session_detail.html", {"campaign": campaign, "session": session, "notes": notes})

def character_detail(request, campaign, character):
    """From campaign and character pk's, return details of a character"""
    campaign = Campaign.objects.get(pk=campaign)
    character = Character.objects.get(pk=character)
    notes = character.notes.all()
    return render(request, "notes/character_detail.html", {"campaign": campaign, "character": character, "notes": notes})
