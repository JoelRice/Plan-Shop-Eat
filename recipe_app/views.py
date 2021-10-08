from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required


from recipe_app.models import Recipe

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