from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.models import Spirit
from lib.flameforged.helpers import render_to

@render_to('profiles/profile.html')
def profile(request):
    title = 'Profile'    
    if request.user.is_authenticated():
        messages = {}
        if not Spirit.objects.filter(message__contributor=request.user.get_profile()).count():
            return {'title': title}
        for spirit in Spirit.objects.filter(message__contributor=request.user.get_profile()):
            messages[spirit] = {}
            messages[spirit]['messages'] = [message for message in spirit.message_set.filter(contributor=request.user.get_profile())]
        return {'messages': messages, 'title': title}
    else:
        return HttpResponseRedirect(reverse('auth_login'))
