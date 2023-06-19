from django.shortcuts import render
from django.views.generic.detail import ListView

from inventory.models import *

# Create your views here.

def home(request):
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = inventory/ingredient_list.html