from django import forms
from .models import Ingredient

class IngredientForm(forms.ModelForm):

    class Meta:

        model = Ingredient
        fields = ('ingredient_name','unit_of_measure')