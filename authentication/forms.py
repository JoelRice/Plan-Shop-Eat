from django import forms
from django.contrib.auth.password_validation import password_validators_help_text_html
from custom_user_app.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    displayname = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text=password_validators_help_text_html()
) 