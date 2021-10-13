from django.db import models
from django.utils import timezone
from custom_user_app.models import CustomUser
# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=25)
    amount = models.FloatField()
    is_spice = models.BooleanField()

    def __str__(self):
        return f"{self.amount} {self.unit} - {self.name}"


class Tool(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owned_by = models.ManyToManyField(
        CustomUser,
        related_name='tool_owned_by',
        blank=True
        )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    instruction = models.TextField()
    cook_time = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recipe_custom_user'
        )
    favorited_by = models.ManyToManyField(
        CustomUser,
        related_name='recipe_favorited_by',
        blank=True
        )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredient'
        )
    tools = models.ManyToManyField(
        Tool,
        related_name='recipe_tool'
        )
    recipe_image = models.URLField(blank=True, null=True)
    recipe_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    int_choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='review_custom_user'
        )
    body = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=int_choices)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='review_recipe'
        )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.recipe} - {self.created_by}'