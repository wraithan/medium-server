import os, math
from django.contrib.auth.models import User
from django.test import Client
from datetime import date
from random import randint, shuffle
from base64 import b64encode
from main.models import Spirit, Message
from profiles.models import Contributor


def rand_str(n):
    return b64encode(os.urandom(int(math.ceil(0.75*n))))[:n]


class Factory(object):
    
    @classmethod
    def get_authenticated_contributor(cls, contributor=None, client=None):
        client = client or Client()
        contributor = contributor or cls.contributor()
        
        passwd = rand_str(8)
        contributor.user.set_password(passwd)
        contributor.user.save()

        assert client.login(username=contributor.user.username, password=passwd)
        return client

    @classmethod
    def spirit(cls, name=None):
        name = name or rand_str(10)
        return Spirit.objects.create(name=name)

    @classmethod
    def message(cls, content=None, author=None, contributor=None, added_on=None, spirit=None, status=None):
        content = content or rand_str(20)
        author = author
        contributor = contributor or cls.contributor()
        added_on = added_on or date.today()
        spirit = spirit or cls.spirit()
        status = status or Message.Status.PENDING
        return Message.objects.create(content=content, author=author, contributor=contributor, added_on=added_on, spirit=spirit, status=status)

    @classmethod
    def contributor(cls, user=None):
        user = User.objects.create(username=rand_str(10), password="", is_active=True)
        return Contributor.objects.create(user=user)
