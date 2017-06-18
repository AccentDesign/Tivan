from django.forms import ModelForm
from .models import Videogame

# Create your views here.


class VideogameForm(ModelForm):
    class Meta:
        model = Videogame
        fields = ('title', 'platform', 'cover', 'available',)