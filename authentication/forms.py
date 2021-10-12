from django import forms

from custom_user_app.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    displayname = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)