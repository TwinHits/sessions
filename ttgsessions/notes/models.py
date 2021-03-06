from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class Campaign(models.Model):
    '''A series of connected sessions of reoccuring characters.'''
    name = models.CharField("Campaign Name", max_length=255)
    date = models.DateTimeField("Start Date")
    swd6 = "Star Wars: D6"
    dnd5 = "Dungeons and Dragons: 5th Edition"
    dnd4 = "Dungeons and Dragons: 4th Edition"
    sweoe = "Star Wars: Edge Of Empire"
    deadlands = "Deadlands"
    system_choices = (
            (swd6, "Star Wars: D6"),
            (dnd5, "Dungeons and Dragons: 5th Edition"),
            (dnd4, "Dungeons and Dragons: 4th Edition"),
            (sweoe, "Star Wars: Edge Of Empire"),
            (deadlands, "Deadlands"),
            )
    system = models.CharField(choices=system_choices, default=None, max_length=255)
    notes = generic.GenericRelation("Note")
    
    def get_last_session_date(self):
        """returns the date of the last session ran for this campaign, or string
        filler to be used instead"""
        sesses = Session.objects.filter(campaign=self)
        if sesses:
           return str(sesses.latest("date").date.date())
        else: 
            return "-"

    def __str__(self):
        return self.name

class Session(models.Model):
    '''A single session of play that has a start date.'''
    date = models.DateTimeField("Session Date")
    notes = generic.GenericRelation("Note")
    campaign = models.ForeignKey(Campaign)
    def __str__(self):
        return str(self.date)[0:10]

class Character(models.Model):
    '''A single character that may appear in multiple sessions in a single campaign'''
    name = models.CharField("Character Name", max_length=255)
    notes = generic.GenericRelation("Note")
    campaign = models.ForeignKey(Campaign)
    def __str__(self):
        return self.name

class Note(models.Model):
    '''A string of text that may be associated with a campaign, a character, or a session'''
    text = models.CharField("Note", max_length=1000)
    date = models.DateTimeField("Date Taken")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        if len(self.text) > 19:
            return self.text[0:19] + "..."
        else: 
            return self.text
