from django.forms import ModelForm
from .models import CollectionItem

# Create your forms here.


class CollectionItemForm(ModelForm):
    class Meta:
        model = CollectionItem
        fields = ('item', 'format',)