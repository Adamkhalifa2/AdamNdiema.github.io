from django import forms
from lib.models import Resources

class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources  # Specify the model for which the form is created
        fields = '__all__'  # Include all fields from the model
