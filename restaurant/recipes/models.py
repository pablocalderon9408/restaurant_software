from django.db import models
from ingredients.models import Ingredient
from utils.models import BaseCreatedModel
from slugify import slugify


class Recipe(BaseCreatedModel):
    name = models.CharField(max_length=50, blank=False)
    slug_name = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    # Guardar recetas con un nombre único (slug name: el nombre usado + _)
    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)
    
    @property
    def total_price(self):
        return sum([ingredient.price for ingredient in self.recipe_ingredients.all()])


class RecipeIngredient(BaseCreatedModel):
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='recipe_ingredients')

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='recipes')

    quantity = models.IntegerField(default=1)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.recipe.name + ": " + self.ingredient.name

    def save(self, *args, **kwargs):
        self.price = self.ingredient.stock.last().price_per_unit * self.quantity
        return super().save(*args, **kwargs)
