from django.shortcuts import render
from django.views.generic import TemplateView


class NewBookView(TemplateView):
    template_name = 'books/book_post_form.html'


class BookDetailView(TemplateView):
    template_name = 'books/book_detail.html'


class BookUpdateView(TemplateView):
    template_name = 'books/book_update_form.html'
