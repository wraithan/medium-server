from django.test import TransactionTestCase, Client
from django.core.urlresolvers import reverse
from nose.tools import istest, assert_equal
from main.models import Spirit, Message
from profiles.models import Contributor
from lib.flameforged.testhelper import Factory


class SmokeTest(TransactionTestCase):

    def setUp(self):
        self.spirits = [Factory.spirit(), Factory.spirit()]
        
    @istest
    def spirit_listing(self):
        client = Client()
        response = client.get(reverse('list_spirits'))
        assert_equal(response.status_code, 200)

