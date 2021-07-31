from django.urls import path

# View
from ingredients import views

urlpatterns = [
    path(
    route='list/',
    view=views.IngredientView.as_view(),
    name='ingredientslist'
    ),

    path(
    route='create/',
    view=views.IngredientCreateView.as_view(),
    name='ingredientcreate'
    ),
]