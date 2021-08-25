from django import forms 
from .models import Profile, User
from django.contrib.auth.models import Group

class SignUPForm(forms.Form): 
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(min_length=8, label='Confirmation Password', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, label='Confirmation Password', widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=163, strip=True, label='First name')
    last_name = forms.CharField(max_length=163, strip=True, label='last name')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']

        if password1 != password2: 
            raise forms.ValidationError('password and confirmation password should be the same.')

        return cleaned_data




    