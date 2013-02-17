from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Maze(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('built at', blank=True, null=True)

    def __unicode__(self):
        return self.name

    def was_built_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(max_length=6, blank=True, null=True)
    maze = models.ForeignKey(Maze)
    north = models.ForeignKey('self', related_name='n', blank=True, null=True)
    south = models.ForeignKey('self', related_name='s', blank=True, null=True)
    east = models.ForeignKey('self', related_name='e', blank=True, null=True)
    west = models.ForeignKey('self', related_name='w', blank=True, null=True)

    def __unicode__(self):
        return self.name
