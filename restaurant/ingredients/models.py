from django.db import models
from utils.models import BaseCreatedModel
from slugify import slugify

class IngredientUnit(BaseCreatedModel):
    name = models.CharField(max_length=50, blank=False)
    slug_name = models.SlugField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)


class Ingredient(BaseCreatedModel):
    name = models.CharField(max_length=50, blank=False)
    slug_name = models.SlugField(max_length=50, blank=True, unique=True)
    units = models.ForeignKey(IngredientUnit, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, separator="_")
        return super().save(*args, **kwargs)

    def __str__(self):
        """Return ingredient"""
        return self.name


class Stock(BaseCreatedModel):
    """Get the total you have from a particular ingredient"""
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE, 
        related_name='stock')
    quantity = models.IntegerField(default=0)
    price_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0)

    def __str__(self):
        """Return ingredient"""
        return f'Stock of {self.ingredient}'

    @property
    def price_per_unit(self):
        """Calculate the cost per unit for every ingredient."""
        return round(self.price_total / self.quantity,2)

    @property
    def total_stock(self):
        self.total = sum([ingredient.price for ingredient in self.recipe_ingredients.all()])
        return self.total
