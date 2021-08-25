# Create your views here.
from pdb import set_trace
from typing import ContextManager
from ingredients.models import Ingredient, IngredientUnit, Stock
from recipes.models import RecipeIngredient
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from ingredients.forms import IngredientUnitForm, StockForm, IngredientForm
# from recipes.models import Recipe_Ingredient

# # Create your views here.

class IngredientUnitCreateView(LoginRequiredMixin, CreateView):
    form_class = IngredientUnitForm
    template_name = 'ingredients/ingredient_unit_create.html'
    success_url = reverse_lazy('ingredients:stocklist')

class IngredientCreateView(LoginRequiredMixin, CreateView):
    form_class = IngredientForm
    template_name = 'ingredients/ingredientcreate.html'
    success_url = reverse_lazy('ingredients:stocklist')

class StockView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'ingredients/ingredients.html'
    model = Stock
    queryset = Stock.objects.all()
    ordering = ('-created',)
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_stock'] = Stock.objects.first()
        return context


class StockCreateView(LoginRequiredMixin, FormView):
    form_class = StockForm
    template_name = 'ingredients/stockcreate.html'
    success_url = reverse_lazy('ingredients:stocklist')

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        #Guardar el formulario asociado
        form.save()
        return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     #Overwrite the method
    #     context = super().get_context_data(**kwargs)
    #     #Get aditional context
    #     context['ingredients'] = Ingredient.objects.all()
    #     context['stock'] = Stock.objects.all()
 
    #     return context