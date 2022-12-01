from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2',)
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',
            'password1': 'Mot de passe',
            'password2': 'Confirmation de mot de passe',
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email',]
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',


        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','phone', 'image']
        labels = {
            'username': 'Pseudo',
            'email': 'Votre adresse e-mail',
            'password1': 'Mot de passe',
            'password2': 'Confirmation de mot de passe',
        }