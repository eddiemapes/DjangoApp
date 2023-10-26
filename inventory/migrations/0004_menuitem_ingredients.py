# Generated by Django 4.2.2 on 2023-10-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_purchase_quantity_purchase_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='ingredients',
            field=models.ManyToManyField(through='inventory.RecipeRequirement', to='inventory.ingredient'),
        ),
    ]
