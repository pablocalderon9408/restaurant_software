from django.db import models
from ingredients.models import Ingredient

# Create your models here.

# Create your models here.
MILILITER = 'ml'
GRAMS = 'g'
UNIT = 'U'

UNIT_CHOICES = [
(MILILITER, "Liter"),
(GRAMS, "Grams"),
(UNIT, "Unit"),
]

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Recipe_Ingredient(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    # @property
    # def cost_per_ingredient(self):
    #     cost_per_ingredient = self.quantity * self.ingredient_name.cost_per_unit
    #     return cost_per_ingredient

