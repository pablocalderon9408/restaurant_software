from django import forms
from ingredients.models import Ingredient, IngredientUnit, Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('ingredient','quantity', 'price_total')

class IngredientUnitForm(forms.ModelForm):

    class Meta:
        model = IngredientUnit
        fields = ('name',)