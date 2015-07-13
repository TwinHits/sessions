from django.contrib import admin
from .models import Campaign, Session, Character, Note

# Register your models here.
admin.site.register(Campaign)
admin.site.register(Session)
admin.site.register(Character)
admin.site.register(Note)
