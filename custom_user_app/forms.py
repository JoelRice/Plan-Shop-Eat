from custom_user_app.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    displayname = forms.CharField(max_length=100, label="Display Name", help_text="Max Length is 100 characters")


    class Meta:
        model = CustomUser
        fields = ('username', 'displayname')

class CustomUserChangeForm(UserChangeForm):
    displayname = forms.CharField(max_length=100, label="DisplayName")

    class Meta:
        model = CustomUser
        fields = ('username', 'displayname')