from main.models import Spirit, Message
from main.forms import MessageForm
from lib.flameforged.helpers import render_to, json_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import HttpResponseBadRequest


@render_to('main/list_spirits.html')
def list_spirits(request):
    spirit_list = Spirit.objects.all()
    title = 'Spirit Listing'
    return locals()

@render_to('main/spirit_random_message.html')
def spirit_random_message(request, spirit):
    spirit = get_object_or_404(Spirit, slug=spirit)
    if spirit.message_set.filter(status=Message.Status.LIVE).count() == 0:
        return HttpResponseBadRequest()
    message = spirit.message_set.filter(status=Message.Status.LIVE).order_by('?')[0]
    return {'message': message, 'title': 'Random Message'}

@json_view
def message_db_json(request):
    if not request.method == 'POST' or not 'spirits' in request.POST:
        return {'result': 'error', 
                'text': "This function requires a POST containing a variable named 'spirits' with the value of a comma seperated list of spirits"}
    spirit_set = Spirit.objects.filter(name__in=request.POST.getlist('spirits'))
    if not spirit_set.count():
        return {'result': 'error',
                'text': 'None of the spirits you requested exist.'}
    retval = {}
    for spirit in spirit_set:
        retval[spirit.name] = serializers.serialize('json', spirit.message_set.filter(status=Message.Status.LIVE))
    return retval

@login_required
@render_to('main/message_add.html')
def message_add(request, spirit):
    spirit = get_object_or_404(Spirit, slug=spirit)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        message = message_form.save(commit=False)
        message.contributor = request.user.get_profile()
        if message.contributor.is_trusted:
            message.status = Message.Status.LIVE
        message.spirit = spirit
        message.save()
    message_form = MessageForm()
    title = 'Message Add'
    return locals()
