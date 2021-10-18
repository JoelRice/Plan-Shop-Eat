from django import forms

from custom_user_app.models import CustomUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    displayname = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput,
        help_text="""Your password can’t be too similar to your other personal information.
                     Your password must contain at least 8 characters.
                     Your password can’t be a commonly used password.
                     Your password can’t be entirely numeric."""
) 