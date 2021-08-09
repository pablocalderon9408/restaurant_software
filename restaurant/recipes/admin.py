"""Recipies admin."""

# Register your models here.
from django.contrib import admin
from django.db import models
from recipes.models import Recipe, RecipeIngredient


class RecipeInline(admin.TabularInline):
    model = RecipeIngredient
    autocomplete_fields = ['ingredient']
    readonly_fields = ['price']
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_price']
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']
    inlines = [RecipeInline]
