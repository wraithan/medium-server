from datetime import date
from django.db import models


class Spirit(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255, null=True, blank=True)
    contributor = models.ForeignKey("profiles.Contributor")
    added_on = models.DateField(default=date.today)
    spirit = models.ForeignKey(Spirit)
