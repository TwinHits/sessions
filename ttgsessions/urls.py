from django.conf.urls import url
from . import views

urlpatterns = [
        url(r"^$", views.sessions_home, name="home"),
        url(r"^(?P<campaign>[0-9]+)/$", views.campaign_detail, name="campaign_detail"),
        url(r"^new/$", views.campaign_new, name="campaign_new"),
        url(r"^(?P<campaign>[0-9]+)/session/(?P<session>[0-9]+)/$", views.session_detail, name="session_detail"),
        url(r"^(?P<campaign>[0-9]+)/session/(?P<character>[0-9]+)/$", views.character_detail, name="character_detail"),
    ]
