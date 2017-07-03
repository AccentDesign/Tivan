from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import MediaItem

# Create your forms here.


class MediaItemForm(ModelForm):
    class Meta:
        model = MediaItem
        fields = ('title', 'platform', 'coverArt', 'available', 'user',)


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active',)


class UserSearchForm(forms.Form):
    username = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserSearchForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
