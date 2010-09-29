from main.models import Spirit
from lib.flameforged.helpers import render_to


@render_to('main/list_spirits.html')
def list_spirits(request):
    spirit_list = Spirit.objects.all()
    return locals()
