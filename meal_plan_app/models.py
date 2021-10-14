from typing import Protocol
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
    plan_title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='meal_plan_created_by'
        )


    @property
    def shopping_list(self):
        # it may be ugly but it works
        all_days = [
            self.monday,
            self.tuesday,
            self.wednesday,
            self.thursday,
            self.friday,
            self.saturday,
            self.sunday
            ]
        list_of_recipes = []
        for day in all_days:
            for recipe in list(day.all()):
                list_of_recipes.append(recipe)
        
        # ingredient specific code
        string_of_ingredients = ",".join([recipe.ingredients for recipe in list_of_recipes])
        ingredients = [ x.strip() for x in string_of_ingredients.split(',') ] # bruh, why though
        ingredients.sort(key=lambda ing: ing.split()[-1]) 
        ing_dict = dict()
        for ing in ingredients:
            if ing not in ing_dict:
                ing_dict[ing] = 1
            else:
                ing_dict[ing] += 1
        ing_list = [f"{v} x {k}" for k, v in ing_dict.items()]

        # tool specific code
        l_o_l = [list(recipe.tools.all()) for recipe in list_of_recipes] # list_of_lists
        flattened_list = []
        for l in l_o_l:
            flattened_list += l
        tools_list=list(set(flattened_list))

        return {'ingredients': ing_list, 'tools': tools_list}


    def __str__(self):
        # I change naming to be more concise.
        return f'{self.plan_title}'