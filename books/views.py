from django.shortcuts import render
from django.views.generic import TemplateView


class NewBookView(TemplateView):
    template_name = 'books/book_post_form.html'


class BookDetailView(TemplateView):
    template_name = 'books/book_detail.html'


class BookUpdateView(TemplateView):
    template_name = 'books/book_update_form.html'


class BookDeleteView(TemplateView):
    template_name = 'books/book_delete_form.html'


class NewCommentView(TemplateView):
    template_name = 'books/comment_form.html'


class UpdateCommentView(TemplateView):
    template_name = 'books/comment_update_form.html'


class UpdateCommentView(TemplateView):
    template_name = 'books/comment_delete_form.html'
