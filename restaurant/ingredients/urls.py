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
        route='stockcreate/',
        view=views.StockCreateView.as_view(),
        name='stockcreate'
    ),
    path(
        route='ingredient/units/create/',
        view=views.IngredientUnitCreateView.as_view(),
        name='ingredient-create'
    ),
    path(
        route='ingredient/create/',
        view=views.IngredientCreateView.as_view(),
        name='ingredient-unit-create'
    ),
]
