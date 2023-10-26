from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import *
from .forms import AddPurchaseForm, CreateIngredientForm, CreateMenuItemForm


# Create your views here.

def home(request):
    # return HttpResponse("Hello world")
    return render(request, "inventory/home.html")

def ingredients(request):
    ingred_list = Ingredient.objects.all().order_by('name')
    return render(request, "inventory/ingredient_list.html", {'ingredients': ingred_list})

def menu(request):
    menu_items = MenuItem.objects.all()
    recipe_requirements = RecipeRequirement.objects.all()
    ingredients = Ingredient.objects.all()
    context = {
        'menu_items': menu_items,
        'recipe_requirements': recipe_requirements,
        'ingredients': ingredients
    }
    return render(request, "inventory/menu.html", context)



def create_purchase(request):
    form = AddPurchaseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            create_purchase = form.save()
            create_purchase.total = create_purchase.quantity * create_purchase.menu_item.price
            create_purchase.save()
            messages.success(request, "Purchase added...")
            return redirect('menu')
    return render(request, 'inventory/create_purchase.html', {'form': form})

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = CreateIngredientForm
    template_name = 'inventory/create_ingredient.html'
    success_url = 'ingredients'

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = CreateMenuItemForm
    template_name = 'inventory/create_menuitem.html'
    success_url = 'menu'



