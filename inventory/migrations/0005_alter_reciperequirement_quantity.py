# Generated by Django 4.2.2 on 2023-10-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_menuitem_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]