# Create your views here.
from recipes.forms import RecipeForm, RecipeIngredientForm
from .models import Ingredient, Recipe, RecipeIngredient
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

# Create your views here.

# class RecipeView(LoginRequiredMixin, ListView):
#     """Return all recipes."""

#     template_name = 'recipes/recipe.html'
#     model = Recipe
#     queryset = Recipe.objects.all()
#     ordering = ('-created',)
#     context_object_name = 'recipes'

class RecipeIngredientView(LoginRequiredMixin, ListView):
    """Return all recipes."""

    template_name = 'recipes/recipe.html'
    model = RecipeIngredient
    queryset = RecipeIngredient.objects.all()
    ordering = ('-created',)
    context_object_name = 'recipes'


class RecipeCreateView(LoginRequiredMixin, FormView):

    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        #Guardar el formulario asociado
        form.save()
        return super().form_valid(form)


class RecipeIngredientCreateView(LoginRequiredMixin, FormView):

    form_class = RecipeIngredientForm
    template_name = 'recipes/recipe_ingredient_create.html'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        #Guardar el formulario asociado
        form.save()
        return super().form_valid(form)