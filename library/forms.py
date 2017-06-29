from django.forms import ModelForm
from .models import MediaItem

# Create your forms here.


class MediaItemForm(ModelForm):
    class Meta:
        model = MediaItem
        fields = ('title', 'platform', 'coverArt', 'available', 'user')