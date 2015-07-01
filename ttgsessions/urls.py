from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.sessions_home, name="home"),
    url(r"^/(?P<pk>[0-9]+)/$", views.campaign_detail, name="campaign_detail"),
    ]
