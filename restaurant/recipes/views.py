# Create your views here.
from .models import Ingredient, Recipe
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

# Create your views here.

class RecipeView(LoginRequiredMixin, ListView):
    """Return all recipes."""

    template_name = 'recipes/recipe.html'
    model = Recipe
    queryset = Recipe.objects.all()
    ordering = ('-created',)
    context_object_name = 'recipes'