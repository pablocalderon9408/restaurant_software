"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from users.views import LandingPage,Home, Sales, Vendors, Expenses, Trial
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name = 'landingpage'),
    path('home/', Home.as_view(), name = 'home'),
    path('sales/', Sales.as_view(), name = 'sales'),
    path('vendors/', Vendors.as_view(), name = 'vendors'),
    path('expenses/', Expenses.as_view(), name = 'expenses'),
    path('users/', include(('users.urls','users'),namespace='users')),
    path('ingredients/', include(('ingredients.urls','ingredients'),namespace='ingredients')),
    path('recipes/', include(('recipes.urls','recipes'),namespace='recipes')),
    path('trial/', Trial.as_view(), name = 'trial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
