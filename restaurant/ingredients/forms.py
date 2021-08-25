from django import forms
from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from ingredients.models import Ingredient, IngredientUnit, Stock


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


class IngredientUnitForm(forms.ModelForm):

    class Meta:
        model = IngredientUnit
        fields = ('name',)

    def clean_name(self):
        data = self.cleaned_data["name"]
        if IngredientUnit.objects.filter(name=data).exists():
            raise forms.ValidationError("Ingredient already exists")
        return data


class IngredientForm(forms.ModelForm):

    units = forms.ModelChoiceField(
        label='Unida de medida',
        queryset=IngredientUnit.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )

    class Meta:
        model = Ingredient
        fields = ('name', 'units')

    def clean_name(self):
        data = self.cleaned_data["name"]
        if Ingredient.objects.filter(name=data).exists():
            raise forms.ValidationError("Ingredient already exists")
        return data
