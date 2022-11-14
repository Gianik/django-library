from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'users/home.html'


class LoginView(TemplateView):
    template_name = 'users/login.html'


class LogoutView(TemplateView):
    template_name = 'users/logout.html'

# Create your views here.
