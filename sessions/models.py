from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.
'''
    A game master can take a note and it will be logged under that particular session.
    A game master can take a note and attach it to a particular character by name.
    A game master can have multiple campaigns running with their own sessions and characters and notes
'''

class Campaign(models.Model):
    '''A series of connected sessions of reoccuring characters.'''
    name = models.CharField("Campaign Name", max_length=255)
    start_date = models.DateTimeField("Start Date")
    system = {
            "swd6": "swd6", 
            "dnd5": "dnd5", 
            "dnd4": "dnd4",
            "sweoe": "sweoe",
            "deadlands": "deadlands", 
            }
    campaign_notes = generic.GenericRelation("Note")
    def __str__(self):
        return self.name

class Session(models.Model):
    '''A single session of play that has a start date.'''
    sess_date = models.DateTimeField("Session Date")
    sessions_notes = generic.GenericRelation("Note")
    campaign = models.ForeignKey(Campaign)
    def __str__(self):
        return str(self.sess_date)[0:10]

class Character(models.Model):
    '''A single character that may appear in multiple sessions in a single campaign'''
    name = models.CharField("Character Name", max_length=255)
    notes = generic.GenericRelation("Note")
    campaign = models.ForeignKey(Campaign)
    def __str__(self):
        return self.name

class Note(models.Model):
    '''A string of text that may be associated with a campaign, a character, or a session'''
    note_text = models.CharField("Note", max_length=1000)
    pub_date = models.DateTimeField("Date Taken")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.note_text[0:19] + "..."
