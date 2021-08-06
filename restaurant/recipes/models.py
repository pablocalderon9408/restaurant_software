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

    def __str__(self):
        return self.recipe_name

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.ManyToManyField(Ingredient,related_name='ingredients')
    quantity = models.FloatField()
    

    def __str__(self):
        return self.recipe.recipe_name

    # def __str__(self):
    #     return self.ingredient_name.ingredient_name

    def bring_variables(self):
        recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
        return recipe.objects.all().ingredient_name






        """Bring the variables from the other models"""

    # @property
    # def cost_per_ingredient(self):
    #     cost_per_ingredient = self.quantity * self.ingredient_name.cost_per_unit
    #     return cost_per_ingredient

