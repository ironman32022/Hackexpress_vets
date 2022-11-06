from django import forms

from .models import *

class AppoinmentForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

