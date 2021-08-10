from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from users.forms import SignupForm

# Create your views here.


class LandingPage(TemplateView):
    template_name = 'landingpage.html'
    # def get(self, request,*args,**kwargs):
    #     return render(request, 'home.html')


class Home(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
# def home(request):
#     return render(request, 'home.html')


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'


class SignupView(FormView):
    """Users sign up view."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
