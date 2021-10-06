from django.db import models
from custom_user_app.models import CustomUser

from recipe_app.models import Recipe
from django.utils import timezone


# Create your models here.

class MealPlan(models.Model):
    monday = models.ManyToManyField(Recipe, related_name='monday_recipe')
    tuesday = models.ManyToManyField(Recipe, related_name='tuesday_recipe')
    wednesday = models.ManyToManyField(Recipe, related_name='wednesday_recipe')
    thursday = models.ManyToManyField(Recipe, related_name='thursday_recipe')
    friday = models.ManyToManyField(Recipe, related_name='friday_recipe')
    saturday = models.ManyToManyField(Recipe, related_name='saturday_recipe')
    sunday = models.ManyToManyField(Recipe, related_name='sunday_recipe')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='meal_plan_created_by'
        )

    def __str__(self):
        return f'{self.created_by} - {self.created_at}'