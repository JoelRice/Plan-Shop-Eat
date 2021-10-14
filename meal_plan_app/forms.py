from django import forms

from recipe_app.models import Recipe

from meal_plan_app.models import MealPlan

class CreateMealPlanForm(forms.Form):
    recipes = Recipe.objects.all()

    plan_title = forms.CharField(max_length=50, required=True)
    monday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    tuesday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    wednesday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    thursday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    friday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    saturday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    sunday = forms.ModelMultipleChoiceField(
        queryset=recipes,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
