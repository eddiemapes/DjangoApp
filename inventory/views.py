from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from inventory.models import *

# Create your views here.

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "inventory/home.html")

def ingredients(request):
    ingred_list = Ingredient.objects.all().order_by('ingredient_name')
    return render(request, "inventory/ingredient_list.html", {'ingredients': ingred_list})

def menu(request):
    menu_list = MenuItem.objects.all()
    return render(request, "inventory/menu.html", {"menuitems": menu_list})

# class IngredientList(ListView):
#     model = Ingredient
#     template_name = "inventory/ingredient_list.html"