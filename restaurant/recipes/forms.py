from recipes.models import Recipe, RecipeIngredient
from ingredients.models import Ingredient
from django import forms


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name',)

    def clean_name(self):
        data = self.cleaned_data["name"]
        if Recipe.objects.filter(name=data).exists():
            raise forms.ValidationError("Recipe name already exists")
        return data


class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        fields = ('recipe', 'ingredient', 'quantity')

    recipe = forms.ModelChoiceField(
        queryset=Recipe.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control', 'required': True})
    )

    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )

    quantity = forms.FloatField(min_value=0)

    def clean_ingredient(self):
        data = self.cleaned_data['ingredient']
        if RecipeIngredient.objects.filter(ingredient=data).exists():
            raise forms.ValidationError("Ingredient already included")
        return data
