from django.db import models
from django.contrib.auth.models import User


class Contributor(models.Model):
    user = models.OneToOneField(User)
