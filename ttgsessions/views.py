from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Campaign, Session, Character, Note 

# Create your views here.

def sessions_home(request):
    """Returns home page of Sessions"""       

    return render(request, "sessions/home.html")
