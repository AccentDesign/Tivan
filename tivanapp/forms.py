from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from library.models import MediaItem

# Create your forms here.


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name"
        self.fields['contact_email'].label = "Email Address"
        self.fields['content'].label = "Message"


class MediaItemForm(ModelForm):
    class Meta:
        model = MediaItem
        fields = ('title', 'platform', 'available',)


class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_active',)
