from django import forms
from django.db import models
from django.forms import widgets

from recipe_app.models import Ingredient, Recipe, Review, Tool

class ToolForm(forms.Form):
    name = forms.CharField(max_length=50)

class IngredientForm(forms.Form):
    name = forms.CharField(max_length=50)
    unit = forms.CharField(max_length=25)
    amount = forms.FloatField()
    is_spice = forms.BooleanField(required=False)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['created_by', 'recipe', 'created_at']


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    instruction = forms.CharField(widget= forms.Textarea)
    cook_time = forms.CharField(max_length=25)
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        )
    tools = forms.ModelMultipleChoiceField(
        queryset=Tool.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    recipe_image = forms.URLField(required=False)
    recipe_description = forms.CharField(widget=forms.Textarea)
