from django.test import TestCase
from django.core.urlresolvers import reverse
from nose.tools import istest, assert_equal
from main.models import Spirit, Message
from profiles.models import Contributor
from lib.flameforged.testhelper import Factory


class SmokeTest(TestCase):

    def setUp(self):
        pass

    def test_spirit_listing(self):
        spirit = Factory.spirit()
        response = self.client.get(reverse('list_spirits'))
        assert_equal(response.status_code, 200)

    def test_spirit_random_message(self):
        spirit = Factory.spirit()
        message = Factory.message(spirit=spirit)
        response = self.client.get(reverse('spirit_random_message',
                                           kwargs={'spirit':spirit.slug}))
        assert_equal(response.status_code, 200)


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

        assert spirit.message_set.all()
