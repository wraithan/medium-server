from django.conf.urls.defaults import *
from django.contrib import admin
from main.views import list_spirits

urlpatterns = patterns('',
    url(r'^spirits/', list_spirits, name='list_spirits'),
)
