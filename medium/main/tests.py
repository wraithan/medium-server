from django.test import TestCase
from django.core.urlresolvers import reverse
from nose.tools import istest, assert_equal
from main.models import Spirit, Message
from profiles.models import Contributor
from lib.flameforged.testhelper import Factory
import json

class SmokeTest(TestCase):

    def setUp(self):
        pass

    def test_spirit_listing(self):
        spirit = Factory.spirit()
        response = self.client.get(reverse('list_spirits'))
        assert_equal(response.status_code, 200)

    def test_spirit_random_message(self):
        message = Factory.message(status=Message.Status.LIVE)
        response = self.client.get(reverse('spirit_random_message',
                                           kwargs={'spirit':message.spirit.slug}))
        assert_equal(response.status_code, 200)

    def test_message_db_json(self):
        spirit1 = Factory.spirit()
        message1 = Factory.message(spirit=spirit1, status=Message.Status.LIVE)
        message2 = Factory.message(spirit=spirit1, status=Message.Status.LIVE)
        spirit2 = Factory.spirit()
        message3 = Factory.message(spirit=spirit1, status=Message.Status.LIVE)
        message4 = Factory.message(spirit=spirit2, status=Message.Status.LIVE)
        response = self.client.post(reverse('message_db_json'),
                                    {
                u'spirits': (spirit1.name, spirit2.name),
                })
        db = json.loads(response.content)
        assert_equal(db['result'], 'ok')
        assert spirit1.name in db.keys()
        assert spirit2.name in db.keys()


class ContributingTest(TestCase):
    
    def setUp(self):
        pass

    def test_that_contributions_are_set_to_pending_by_default(self):
        contributor = Factory.contributor()
        Factory.get_authenticated_contributor(contributor=contributor, client=self.client)
        spirit = Factory.spirit()
        assert not spirit.message_set.all()

        response = self.client.post(reverse('message_add', 
                                            kwargs={'spirit':spirit.slug}),
                                    {
                u'content': 'This is from beyond',
                u'author': '',
                })
        assert_equal(response.status_code, 200)

        spirit = Spirit.objects.get(id=spirit.id)

        assert spirit.message_set.filter(status=Message.Status.PENDING)
