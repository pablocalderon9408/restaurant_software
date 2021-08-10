# Create your views here.
from ingredients.models import Ingredient, Stock
from recipes.models import RecipeIngredient
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
# from recipes.models import Recipe_Ingredient

# # Create your views here.

class StockView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'ingredients/ingredients.html'
    model = Stock
    queryset = Stock.objects.all()
    ordering = ('-created',)
    context_object_name = 'ingredients'

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name','units']
    template_name = 'ingredients/ingredientcreate.html'
    success_url = reverse_lazy('ingredients:stocklist')