from django.urls import path

# View
from users import views


urlpatterns = [

    path(
        route='',
        view=views.Home.as_view(),
        name='home'
    ),
        # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'),

    path(
        route='password-recovery/',
        view=views.PasswordRecoveryView.as_view(),
        name='password_recovery'),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'),

    path(
    route='logout/',
    view=views.LogoutView.as_view(),
    name='logout'),
    
]



