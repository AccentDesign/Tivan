from django.forms import ModelForm
from .models import Videogame

# Create your forms here.


class VideogameForm(ModelForm):
    class Meta:
        model = Videogame
        fields = ('title', 'cover',)