from django import forms
from django.forms import ModelForm, TextInput

from .models import *

class cityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name',)
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}