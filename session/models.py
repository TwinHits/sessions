from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.
'''
    A game master can take a note and it will be logged under that particular session.
    A game master can take a note and attach it to a particular character by name.
'''

class Session(models.Model):
    '''A single session of play that has a start date.'''
    sess_date = models.DateTimeField("Session Date")
    notes = generic.GenericRelation("Note")
    def __str__(self):
        return str(self.sess_date)[0:9]

class Character(models.Model):
    name = models.CharField("Name", max_length=1000)
    notes = generic.GenericRelation("Note")
    def __str__(self):
        return self.name

class Note(models.Model):
    note_text = models.CharField("Note", max_length=1000)
    pub_date = models.DateTimeField("Date Taken")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    def __str__(self):
        return self.note_text[0:19] + "..."
