# Create your views here.
from .models import Ingredient
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
# from recipes.models import Recipe_Ingredient

# # Create your views here.

class IngredientView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'ingredients/ingredients.html'
    model = Ingredient
    queryset = Ingredient.objects.all()
    ordering = ('-created',)
    context_object_name = 'ingredients'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['ingredient_name','unit_of_measure']
    template_name = 'ingredients/ingredientcreate.html'
    success_url = reverse_lazy('ingredients:ingredientslist')