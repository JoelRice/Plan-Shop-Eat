from django.db import models
from django.utils import timezone
from recipe_app.models import Tool, Ingredient
from meal_plan_app.models import MealPlan
# Create your models here.

class ShoppingList(models.Model):
    tools = models.ManyToManyField(Tool, related_name='shopping_list_tools')
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='shopping_list_ingredient'
        )
    meal_plan = models.ForeignKey(
        MealPlan,
        on_delete=models.CASCADE,
        related_name='shopping_list_meal_plan'
        )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.created_at}'
