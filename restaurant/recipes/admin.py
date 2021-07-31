from django.contrib import admin
from .models import Recipe, Recipe_Ingredient

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Recipe_Ingredient)
