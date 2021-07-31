from django.db import models

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

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50, blank=False)
    unit_of_measure = models.CharField(max_length=20,choices=UNIT_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.ingredient_name

class Stock(models.Model):
    """Get the total you have from a particular ingredient"""
    ingredient_name = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.FloatField()
    total_cost = models.FloatField()
    
    @property
    def cost_per_unit(self):
        """ Calculate the cost per unit for every ingredient """
        cost_per_unit = self.total_cost / self.quantity
        return cost_per_unit