from django import forms
from django.db import models
from django.forms import widgets

from recipe_app.models import Recipe, Review, Tool

class ToolForm(forms.Form):
    name = forms.CharField(max_length=50)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['created_by', 'recipe', 'created_at']


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        help_text = "<a href='/recipe_app/createTool/?next=/recipe_app/createRecipe/'>Add new tool</a>"
    )
    instructions = forms.CharField(widget= forms.Textarea)
    cook_time = forms.CharField(max_length=25)
    ingredients = forms.CharField(
        widget= forms.Textarea, 
        help_text='Add ingredients seprated by commas e.g. "1 cup milk, 1 egg, 1 packet of Koolaid"'
        )
    recipe_image = forms.URLField(required=False)
    recipe_description = forms.CharField(widget=forms.Textarea)
