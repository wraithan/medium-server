from django.conf.urls.defaults import *
from django.contrib import admin
from main.views import list_spirits, message_add
import dselector

parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('',
    url(r'spirits/', list_spirits, name='list_spirits'),
    url(r'{spirit:slug}/add', message_add, name='message_add'),
)
