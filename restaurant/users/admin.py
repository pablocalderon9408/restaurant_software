from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Profile

# Register your models here.

admin.site.register(Profile)
