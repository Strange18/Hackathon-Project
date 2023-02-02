from django import forms
from django.db.models import fields
from .models import *

class complain_form(forms.ModelForm):
    class Meta:
        model = complain
        fields = ['title','description','image','municipality','severity','department']

class idea_form(forms.ModelForm):
    class Meta:
        model = idea
        fields = ['title','description','image']
