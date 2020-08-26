from django import forms
from  django.forms import ModelForm

from .models import *

class dutyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : 'Create your new tasks..'}))
    class Meta():
        model = duty
        fields = '__all__'
        exclude = ['notes']