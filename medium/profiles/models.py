from django.db import models
from django.contrib.auth.models import User
from main.models import Message


class Contributor(models.Model):
    class Status:
        TRUSTED = 1
        NEUTRAL = 2
        SPAMMER = 3
        CHOICES = (
            (TRUSTED, 'Trusted'),
            (NEUTRAL, 'Neutral'),
            (SPAMMER, 'Spammer'),
            )
    user = models.OneToOneField(User)
    status = models.IntegerField(choices=Status.CHOICES, default=Status.NEUTRAL)

    @property
    def is_trusted(self):
        if self.status == self.Status.TRUSTED:
            return True
        else:
            if self.message_set.count() >= 10:
                if (self.message_set.filter(status=Message.Status.LIVE).count()/(self.message_set.count())) >= 0.9:
                    return True
                else:
                    return False
