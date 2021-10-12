from django import forms

from recipe_app.models import Review

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