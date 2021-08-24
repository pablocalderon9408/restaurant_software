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
    route='stock/create/',
    view=views.StockCreateView.as_view(),
    name='stockcreate'
    ),
    path(
    route='ingredient/create/',
    view=views.IngredientUnitCreateView.as_view(),
    name='ingredientcreate'
    ),
]
