from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("/ingredients", views.IngredientList.as_view(), name="ingredients"),
    path("ingredients", views.ingredients, name="ingredients"),
    path("menu", views.menu, name="menu"),
    path('create_purchase/', views.create_purchase, name="create_purchase"),
    path('create_ingredient', views.IngredientCreateView.as_view(), name="create_ingredient"),
    path('create_menuitem', views.MenuItemCreateView.as_view(), name="create_menuitem"),
]