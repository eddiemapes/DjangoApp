from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=25, null=False, blank=False)
    ingredient_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    unit = models.CharField(max_length=10, null=False, blank=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class MenuItem(models.Model):
    menuitem_name = models.CharField(max_length=25, null=False, blank=False)
    menuitem_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    