from django.urls import path

# View
from ingredients import views

urlpatterns = [
    path(
    route='stock/',
    view=views.StockView.as_view(),
    name='stocklist'
    ),

    path(
    route='create/',
    view=views.IngredientCreateView.as_view(),
    name='ingredientcreate'
    ),
]
