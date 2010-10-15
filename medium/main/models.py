from datetime import date
from django.db import models
from django.template.defaultfilters import slugify

class Spirit(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Spirit, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Message(models.Model):
    class Status:
        LIVE = 1
        PENDING = 2
        REJECTED = 3
        CHOICES = (
            (LIVE, 'Live'),
            (PENDING, 'Pending'),
            (REJECTED, 'Rejected'),
            )
    content = models.TextField()
    author = models.CharField(max_length=255, null=True, blank=True)
    contributor = models.ForeignKey("profiles.Contributor")
    added_on = models.DateField(default=date.today)
    spirit = models.ForeignKey(Spirit)
    status = models.IntegerField(choices=Status.CHOICES, default=Status.PENDING)

    def __unicode__(self):
        return "%s - %s - %s" % (self.content, self.author, self.spirit)
