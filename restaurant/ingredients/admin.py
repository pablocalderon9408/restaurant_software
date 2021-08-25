

# Register your models here.
from django.contrib import admin
from .models import IngredientUnit, Ingredient, Stock

# Register your models here.


@admin.register(IngredientUnit)
class IngredientUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_name']
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']
    extra = 0


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_name', 'units']
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['ingredient', 'quantity','price_total']
    search_fields = ['ingredient__name']
    autocomplete_fields = ['ingredient']
