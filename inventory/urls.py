from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("/ingredients", views.IngredientList.as_view(), name="ingredients"),
    path('ingredients', views.ingredients, name='ingredients'),
    path('menu', views.menu, name='menu'),
    path('purchases', views.purchases, name='purchases'),
    path('create_purchase/', views.create_purchase, name="create_purchase"),
    path('create_ingredient', views.IngredientCreateView.as_view(), name="create_ingredient"),
    path('create_menuitem', views.MenuItemCreateView.as_view(), name="create_menuitem"),
    path('create_reciperequirement', views.RecipeRequirementCreateView.as_view(), name="create_reciperequirement"),
    path('incomereport', views.incomereport, name='incomereport'),
    path('modify_ingredient/<int:id>/', views.modify_ingredient, name='modify_ingredient'),
    path('delete_ingredient/<int:id>/', views.delete_ingredient, name='delete_ingredient')
]