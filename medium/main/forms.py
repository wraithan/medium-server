from django.forms import ModelForm
from main.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('content', 'author')
    
