from django.db import models
from recipe_app.models import Tool, Ingredient
from meal_plan_app.models import MealPlan
# Create your models here.

class ShoppingList(models.Model):
    tools = models.ManyToManyField(Tool, related_name='shopping_list_tools')
    ingredient = models.ManyToManyField(
        Ingredient,
        related_name='shopping_list_ingredient'
        )
    meal_plan = models.ForeignKey(
        MealPlan,
        on_delete=models.CASCADE,
        related_name='shopping_list_meal_plan'
        )

    def __str__(self):
        return self.meal_plan
