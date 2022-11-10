from django.urls import path
from .api import BookViewSet
from .views import NewBookView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('new/', NewBookView.as_view(), name='new-book'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('', BookViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='book-list'),
    path('book-detail/<int:pk>', BookViewSet.as_view({
        'get': 'retrieve',
    }), name='book-detailset'),
    path('update/detail/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve2',
        'post': 'update'
    }), name='book-detailupdateinfo'),
    path('book-delete/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve3',
        'post': 'destroy'
    }), name='book-deletepage'),





]
