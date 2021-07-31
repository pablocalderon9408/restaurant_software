from django.urls import path

# View
from recipes import views

urlpatterns = [
    path(
    route='list/',
    view=views.RecipeView.as_view(),
    name='recipeslist'
    ),
]