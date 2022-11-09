from django.shortcuts import render
from django.views.generic import TemplateView


class NewBookView(TemplateView):
    template_name = 'books/book_post_form.html'
