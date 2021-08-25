from pdb import set_trace
from django import forms
from django.db.models import query
from django.forms.fields import ChoiceField
from django.forms.widgets import Select
from ingredients.models import Ingredient, IngredientUnit, Stock


UNIT_CHOICES = []


for i in IngredientUnit.objects.all():
    UNIT_CHOICES.append(i.name)
    



class StockForm(forms.Form):
    #Ingredient field
    ingredient = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Nombre del ingrediente','class': 'form-control','required': True})
    )

    #IngredientUnit field
    units = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Unidad de medida','class': 'form-control','required': True})
    )

    # units = forms.ChoiceField(
    #     choices=UNIT_CHOICES,
    #     widget=forms.Select(),
    # )

    #Stock fields
    quantity = forms.FloatField(min_value=0)
    price_total = forms.FloatField(min_value=0)

    def clean_ingredient(self):
        #Este méodo nos permite hacer la validación de un campo en especifico.
        #Coger el dato ingresado por quien llenó el formulario.
        ingredient = self.cleaned_data['ingredient']

        #Hago una consulta en la query, usando exists que devuelve un booleano
        query = Ingredient.objects.filter(name=ingredient).exists()

        #Si el query es True, quiere decir que ese ingrediente ya está en uso
        if query:
            raise forms.ValidationError('Ingredient is already in the database.')
        return ingredient
    
    def save(self):
        #Retrieve all the data
        data = self.cleaned_data

        #Ingredient.name
        ingredient = data['ingredient']
        #IngredientUnit.name
        units = data['units']
        #Stock.quantity
        quantity = data['quantity']
        #Stock.price_total
        price_total = data['price_total']

        query = IngredientUnit.objects.filter(name=units).exists()

        if query:
            z = IngredientUnit.objects.get(name=units)
            b = Ingredient(name=ingredient, units = z)
            b.save()
            c = Stock(ingredient=b, quantity=quantity, price_total=price_total)
            c.save()
        else:
            a = IngredientUnit(name=units)
            a.save()
            b = Ingredient(name=ingredient, units = a)
            b.save()
            c = Stock(ingredient=b, quantity=quantity, price_total=price_total)
            c.save()

        
        # import pdb; pdb.set_trace()

        # a = IngredientUnit(name=units)
        # a.save()

        # b = Ingredient(name=ingredient, units = z)
        # b.save()

        # c = Stock(ingredient=b, quantity=quantity, price_total=price_total)
        # c.save()

class IngredientUnitForm(forms.ModelForm):

    class Meta:
        model = IngredientUnit
        fields = ('name',)