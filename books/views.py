from django.shortcuts import render
from django.views.generic import TemplateView


class NewBookView(TemplateView):
    template_name = 'book_post_form.html'
