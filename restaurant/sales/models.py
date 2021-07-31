from django.db import models

# Create your models here.

# Create your models here.
LITER = 'L'
KILOGRAMS = 'Kg'
GRAMS = 'g'
UNIT = 'U'

UNIT_CHOICES = [
(LITER, "Liter"),
(KILOGRAMS, "Kilograms"),
(GRAMS, "Grams"),
(UNIT, "Unit"),
]

class Sale(models.Model):
    customer_name = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


# Calculated fields: order (how to have a list with the diferent menu products?), state_of_sale (create all the environment to change the status), price, payment_method.

    def cost_per_ingredient(self):
        cost_per_ingredient = self.ingredient_quantity
        return cost_per_ingredient

    def __str__(self):
        """Return username."""
        return self.sale
