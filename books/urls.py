from django.urls import path
from .api import BookViewSet
from .views import NewBookView

urlpatterns = [
    path('new/', NewBookView.as_view(), name='new-book'),
    path('', BookViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='book-list')



]
