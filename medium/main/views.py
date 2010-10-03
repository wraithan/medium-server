from main.models import Spirit
from main.forms import MessageForm
from lib.flameforged.helpers import render_to
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@render_to('main/list_spirits.html')
def list_spirits(request):
    spirit_list = Spirit.objects.all()
    return locals()

@render_to('main/spirit_random_message.html')
def spirit_random_message(request, spirit):
    spirit = get_object_or_404(Spirit, slug=spirit)
    message = spirit.message_set.all().order_by('?')[0]
    return {'message': message}

@login_required
@render_to('main/message_add.html')
def message_add(request, spirit):
    spirit = get_object_or_404(Spirit, slug=spirit)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        message = message_form.save(commit=False)
        message.contributor = request.user.get_profile()
        message.spirit = spirit
        message.save()
    message_form = MessageForm()
    return locals()
