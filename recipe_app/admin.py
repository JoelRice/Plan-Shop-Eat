from django.contrib import admin
from recipe_app.models import Review, Tool, Ingredient, Recipe


# Register your models here.

admin.site.register(Tool)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Review)