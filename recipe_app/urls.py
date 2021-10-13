from django.urls import path

from recipe_app.views import (
    CreateIngredientView,
    CreateRecipeView,
    CreateReviewView,
    CreateToolView,
    logged_in_view,
    add_favorite_view,
    recipe_view
    )
from recipe_app.views import remove_favorite_view

urlpatterns = [
    path('recipe/<int:id>/', recipe_view, name='recipe' ),
    path('recipes/', logged_in_view, name='recipes'),
    path("favorite/<int:id>/", add_favorite_view, name="favorite"),
    path("removeFavorite/<int:id>/", remove_favorite_view, name="remove_favorite"),
    path('createTool/', CreateToolView.as_view(), name='create_tool'),
    path('createIngredient/', CreateIngredientView.as_view(), name='create_ingredient'),
    path('createReview/<int:id>/', CreateReviewView.as_view(), name='create_review'),
    path('createRecipe/', CreateRecipeView.as_view(), name='create_recipe'),
]