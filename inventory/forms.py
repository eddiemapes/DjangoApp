from .models import *
from django.forms import ModelForm


class AddPurchaseForm(ModelForm):
    class Meta:
        model = Purchase 
        fields = ['menu_item', 'quantity']

class CreateIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CreateMenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CreateRecipeRequirementForm(ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'