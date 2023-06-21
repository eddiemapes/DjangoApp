from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("/ingredients", views.IngredientList.as_view(), name="ingredients"),
    path("/ingredients", views.ingredients, name="ingredients"),
]