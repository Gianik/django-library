from django.urls import path
from .api import BookViewSet, CommentsViewSet
from .views import NewBookView, BookDetailView, BookUpdateView, BookDeleteView, NewCommentView, UpdateCommentView, DeleteCommentView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('new/', login_required(NewBookView.as_view()), name='new-book'),
    path('detail/<int:pk>', login_required(BookDetailView.as_view()),
         name='book-detail'),
    path('update/<int:pk>', login_required(BookUpdateView.as_view()),
         name='book-update'),
    path('delete/<int:pk>', login_required(BookDeleteView.as_view()),
         name='book-delete'),
    path('new/comment/<int:pk>',
         login_required(NewCommentView.as_view()), name='book-comment'),
    path('update/comment/<int:pk>', login_required(UpdateCommentView.as_view()),
         name='book-comment-update'),
    path('delete/comment/<int:pk>', login_required(DeleteCommentView.as_view()),
         name='book-comment-delete'),
    path('', login_required(BookViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })), name='book-list'),
    path('book-detail/<int:pk>', login_required(BookViewSet.as_view({
        'get': 'retrieve',
    })), name='book-detailset'),
    path('update/detail/<int:pk>/', login_required(BookViewSet.as_view({
        'get': 'retrieve2',
        'post': 'update'
    })), name='book-detailupdateinfo'),
    path('book-delete/<int:pk>/', login_required(BookViewSet.as_view({
        'get': 'retrieve3',
        'post': 'destroy'
    })), name='book-deletepage'),
    path('borrow-return/<int:pk>/', login_required(BookViewSet.as_view({
        'get': 'borrow_return_book',
    })), name='book-borrow-return'),
    path('new-comment/<int:pk>/', login_required(CommentsViewSet.as_view({
        'get': 'retrieve',
        'post': 'create'
    })), name='book-new-comment'),
    path('update-comment/<int:pk>/', login_required(CommentsViewSet.as_view({
        'get': 'retrieve',
        'post': 'update'
    })), name='book-update-comment'),
    path('delete-comment/<int:pk>/', login_required(CommentsViewSet.as_view({
        'post': 'destroy'
    })), name='book-destroy-comment'),





]
