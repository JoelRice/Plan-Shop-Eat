# Generated by Django 3.2.8 on 2021-10-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0008_alter_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
