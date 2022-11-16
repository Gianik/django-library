from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'users/home.html'


class LoginView(TemplateView):
    template_name = 'users/login.html'


class LogoutView(TemplateView):
    template_name = 'users/logout.html'


class RegisterView(TemplateView):
    template_name = 'users/register.html'


class DashboardView(TemplateView):
    template_name = 'users/dashboard.html'


class EditProfileView(TemplateView):
    template_name = 'users/edit_profile.html'
# Create your views here.
