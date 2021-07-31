

# Register your models here.
from django.contrib import admin
from .models import Ingredient, Stock

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Stock)