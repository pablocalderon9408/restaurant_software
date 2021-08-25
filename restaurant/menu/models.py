from django.db import models
from utils.models import BaseCreatedModel
from recipes.models import Recipe

# Create your models here.
class Menu(BaseCreatedModel):
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE, 
        related_name='menu_recipe')

    description = models.TextField(max_length=800)

    price_to_customer = models.IntegerField()