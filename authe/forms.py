from dataclasses import field
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registerform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    

class loginForm(forms.Form):
    username = forms.CharField(max_length= 100)
    password = forms.CharField(widget= forms.PasswordInput())

    widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.Textarea(attrs={'class':'form-control'}),
        }
    
