from django import forms
from django.db.models import fields
from .models import *

class question_form(forms.ModelForm):
    class Meta:
        model = question
        fields = ['title','description','image']

class answer_form(forms.ModelForm):
    class Meta:
        model = answers
        fields = ['description','image']

