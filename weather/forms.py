from django import forms
from django.forms import ModelForm

from .models import *

class cityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name',)