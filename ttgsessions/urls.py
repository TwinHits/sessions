from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.sessions_home, name="sessions_home"),
    ]
