from django.db import models
from django.contrib.auth.models import AbstractUser, User
from utils.models import BaseCreatedModel

# Create your models here.

# class User(AbstractUser):
#     country = models.CharField(max_length=50)
    

class Profile(BaseCreatedModel):

    #Django has just 1 class of user. Superuser and staff are user objects with special attributes. In the same way, profile is an extension of the user model. One way to think about the need of the Profile class is to understand that whenever you want to create an user, you must need an object to assign it to.

    #User attributes
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)

    def __str__(self):
        """Return username."""
        return self.user.username
