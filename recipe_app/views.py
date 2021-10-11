from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from recipe_app.forms import IngredientForm, ToolForm



from recipe_app.models import Ingredient, Recipe, Tool

# Create your views here.


@login_required
def logged_in_view(request):
    recipes = Recipe.objects.all()

    return render(
        request,
        'recipes.html',
        {'recipes': recipes}
        )


@login_required
def add_favorite_view(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.favorited_by.add(request.user)

    return HttpResponseRedirect(
        request.META.get('HTTP_REFERER'),
        reverse('recipes')
        )

@login_required
def remove_favorite_view(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.favorited_by.remove(request.user)

    return HttpResponseRedirect(
        request.META.get('HTTP_REFERER'),
        reverse('recipes')
        )


def recipe_view(request, id):
    recipe = Recipe.objects.get(id=id)
    reviews = recipe.review_recipe.all()

    return render(
        request,
        'recipe.html',
        {
            'recipe': recipe,
            'reviews': reviews
            }
        )


class CreateToolView(View):
    template_name = 'generic_form.html'
    form = ToolForm()

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request):
        form = ToolForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Tool.objects.filter(name=data.get('name')).exists():
                return render(
                    request,
                    self.template_name,
                    {
                        'form': self.form,
                        'error': f"{data.get('name')} already exists in the database."
                        }
                )
            tool = Tool.objects.create(name=data.get('name'))
            return HttpResponseRedirect(
                request.META.get('HTTP_REFERER'),
                reverse('recipes')
                )
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )


class CreateIngredientView(View):
    template_name = 'generic_form.html'
    form = IngredientForm()

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request):
        form = IngredientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tool = Ingredient.objects.create(
                name=data.get('name'),
                unit=data.get('unit'),
                amount=data.get('amount'),
                is_spice=data.get('is_spice')
                )
            return HttpResponseRedirect(
                request.META.get('HTTP_REFERER'),
                reverse('recipes')
                )
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )
