from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from recipe_app.forms import IngredientForm, RecipeForm, ReviewForm, ToolForm



from recipe_app.models import Ingredient, Recipe, Review, Tool

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

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
            ingredient = Ingredient.objects.create(
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


class CreateReviewView(View):
    template_name = 'generic_form.html'
    form = ReviewForm()

    def get(self, request, id):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request, id):
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.get(id=id)
            user = request.user
            review = Review.objects.create(
                recipe = recipe,
                created_by = user,
                body = data.get('body'),
                rating = data.get('rating'),
            )
            return HttpResponseRedirect(
                reverse('recipe', args=(id,))
                )
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )


class CreateRecipeView(View):
    template_name = 'generic_form.html'
    form = RecipeForm()

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            recipe = Recipe.objects.create(
                created_by = user,
                title = data.get('title'),
                instruction = data.get('instruction'),
                cook_time = data.get('cook_time'),
                # ingredients = data.get('ingredients'),
                # tools = data.get('tools'),
                recipe_image = data.get('recipe_image'),
                recipe_description = data.get('recipe_description'),
            )
            recipe.ingredients.set(data.get('ingredients'))
            recipe.tools.set(data.get('tools'))
            return HttpResponseRedirect(
                reverse('recipe', args=(recipe.id,))
                )
        return render(
            request,
            self.template_name,
            {'form': self.form}
        )
