from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from ingredients.models import Ingredient, IngredientUnit, Stock
from django.core.exceptions import ValidationError


UNIT_CHOICES = []


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('ingredient', 'quantity', 'price_total')
        
    #Ingredient field
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )

    #Stock fields
    quantity = forms.FloatField(min_value=0)
    price_total = forms.FloatField(min_value=0)

    def clean_ingredient(self):
        data = self.cleaned_data['ingredient']
        if Stock.objects.filter(ingredient=data).exists():
            raise forms.ValidationError("Ingredient already exists")
        return data


class IngredientUnitForm(forms.ModelForm):

    class Meta:
        model = IngredientUnit
        fields = ('name',)

    def clean_name(self):
        data = self.cleaned_data["name"]
        if IngredientUnit.objects.filter(name=data).exists():
            raise forms.ValidationError("Ingredient unit already exists")
        return data


class IngredientForm(forms.ModelForm):

    units = forms.ModelChoiceField(
        label='Unidad de medida',
        queryset=IngredientUnit.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'units')

    def clean_name(self):
        data = self.cleaned_data["name"]
        if Ingredient.objects.filter(name=data).exists():
            print("me fui por acá")
            import pdb;pdb.set_trace()
            raise forms.ValidationError("Ingredient already exists")
        return data
