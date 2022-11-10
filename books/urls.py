from django.urls import path
from .api import BookViewSet
from .views import NewBookView, BookDetailView, BookUpdateView

urlpatterns = [
    path('new/', NewBookView.as_view(), name='new-book'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='book-list'),
    path('book-detail/<int:pk>', BookViewSet.as_view({
        'get': 'retrieve',
    }), name='book-detailset'),
    path('book-update/detail/<int:pk>', BookViewSet.as_view({
        'get': 'retrieve2',
        'post': 'update'
    }), name='book-detailupdateinfo'),




]
