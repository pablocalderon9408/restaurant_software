from menu.models import Menu
from django.db import models
from django.db.models.aggregates import Max
from utils.models import BaseCreatedModel
from slugify import slugify
# Create your models here.

PAYMENT_METHODS = [
    ('TC', "Credit Card"),
    ('QR', "Transferencia o QR"),
    ('EFE', "Efectivo"),
    ('TD', "Tarjeta débito"),
]


class Sale(BaseCreatedModel):
    customer_name = models.CharField(max_length=50, blank=True)
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=25)
    menu = models.ForeignKey(
        Menu, 
        on_delete=models.CASCADE, 
        related_name='sale_menu',
        default=None
    )
    quantity_ordered = models.IntegerField()
    discount = models.FloatField(default=0)


    def __str__(self):
        return f'Sale {self.pk} was successfully created'

    

    # def save(self, *args, **kwargs):
    #     """Create the slug name of the objects created in the model: IngredientUnit"""
    #     self.slug_name = slugify(self.name, separator="_")
    #     return super().save(*args, **kwargs)

