from django.forms import ModelForm
from . models import Setlist

class SetlistForm(ModelForm):
    class Meta:
        model = Setlist
        fields = ['gig', 'song']