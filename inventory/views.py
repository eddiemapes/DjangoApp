from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import AddPurchaseForm, CreateIngredientForm, CreateMenuItemForm, CreateRecipeRequirementForm


# Create your views here.

class SignupView(CreateView):
    template_name = 'inventory/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login_page')
    




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('menu')

    return render(request, 'inventory/login_page.html', {})







def home(request):
    # return HttpResponse("Hello world")
    return render(request, "inventory/home.html")

def ingredients(request):
    ingred_list = Ingredient.objects.all().order_by('name')
    return render(request, "inventory/ingredient_list.html", {'ingredients': ingred_list})






def modify_ingredient(request, id):
    ingredient = Ingredient.objects.get(pk=id)
    
    if request.method == 'POST':
        form = CreateIngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
        return redirect('ingredients')
    else:
        form = CreateIngredientForm(instance=ingredient)
        context = {'form': form,
                   'ingredient': ingredient}
        return render(request, 'inventory/modify_ingredient.html', context)

def delete_ingredient(request, id):
    
    ingredient = Ingredient.objects.get(pk=id)
    ingredient.delete()
    return redirect('ingredients')
    

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


def purchases(request):
    purchases = Purchase.objects.all()
    context = {'purchases':purchases}

    return render(request, 'inventory/purchases.html', context)



def create_purchase(request):
    form = AddPurchaseForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            create_purchase = form.save()
            create_purchase.total = create_purchase.quantity * create_purchase.menu_item.price
            create_purchase.save()

            menu_item_id = request.POST.get('menu_item')
            quantity = int(request.POST.get('quantity'))
            menu_item = MenuItem.objects.get(pk=menu_item_id)
            
            cogs = calculate_cogs(menu_item, quantity)
            create_purchase.cogs = cogs
            create_purchase.save()

            quantitypurchased = create_purchase.quantity
            # Change the ingredient inventory
            for requirement in menu_item.ingredients.through.objects.filter(item=menu_item):
                ingredient = requirement.ingredient
                quantityofingredientrequired = requirement.quantity
                ingredient.quantity -= quantityofingredientrequired * quantitypurchased
                ingredient.save()

            messages.success(request, "Purchase added...")
            return redirect('purchases')
    context = {'form': form,}
    return render(request, 'inventory/create_purchase.html', context)

def calculate_cogs(menu_item, quantity):
    cogsperingredient = 0
    for requirement in menu_item.ingredients.through.objects.filter(item=menu_item):
        ingredient = requirement.ingredient
        quantityofingredientrequired = requirement.quantity
        unitpriceofingredient = ingredient.unit_price
        cogsperingredient += quantityofingredientrequired * unitpriceofingredient
    cogs = cogsperingredient * quantity
    return cogs

def incomereport(request):
    purchases = Purchase.objects.all()
    revtotal = 0
    expensetotal = 0
    for purchase in purchases:
        revtotal += purchase.total
        expensetotal += purchase.cogs
    overalltotal = revtotal - expensetotal

    context = {'purchases': purchases,
               'revtotal': revtotal,
               'expensetotal': expensetotal,
               'overalltotal': overalltotal
               }

    return render(request, 'inventory/incomereport.html', context)

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

class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = CreateRecipeRequirementForm
    template_name = 'inventory/create_reciperequirement.html'
    success_url = 'menu'


