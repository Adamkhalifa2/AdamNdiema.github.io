from django import forms
from port.models import Contact


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
