from django.conf.urls.defaults import *
from django.contrib import admin
from main import views
import dselector

parser = dselector.Parser()
url = parser.url

urlpatterns = parser.patterns('',
                              url(r'spirits/', 
                                  views.list_spirits, 
                                  name='list_spirits'),
                              
                              url(r'{spirit:slug}/add', 
                                  views.message_add, 
                                  name='message_add'),
                              
                              url(r'{spirit:slug}/random',
                                  views.spirit_random_message,
                                  name='spirit_random_message'),
                              
)
