# Generated by Django 3.2.8 on 2021-10-06 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='measurement',
            new_name='unit',
        ),
    ]