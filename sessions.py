#django imports
from django.utils import timezone
from django.conf import settings as django_settings
from ttghelper import settings as ttghelper_settings
django_settings.configure(ttghelper_settings)

#sessions imports
from ttgsessions.models import Campaign, Session, Character, Note

#other imports
from sys import argv

def session_start():
    '''requests campaign name from the user in order to categorize later actions'''
    campaign = input("Campaign:")
    if not Campaign.objects.get(name=campaign):
        if input("This campaign is unknown. Create new?").upper() == "YES" or "Y":
           campaign = Campaign.create(name=campaign, start_date=timezone.now())
           #campaign.save()
        else:
            session_start()
    else:
        campaign = Campaign.objects.get(name=campaign)
    return campaign 

if __name__ == "__main__":
    if argv[1] == "start":
        session_start()
