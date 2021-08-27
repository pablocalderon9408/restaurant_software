from django.urls import path

# View
from recipes import views

urlpatterns = [
    path(
    route='',
    view=views.RecipeIngredientView.as_view(),
    name='recipeslist'
    ),

    path(
    route='recipe/create/',
    view=views.RecipeCreateView.as_view(),
    name='recipe-create'
    ),


    path(
    route='recipe-ingredient/create/',
    view=views.RecipeIngredientCreateView.as_view(),
    name='recipe-ingredient-create'
    ),



]