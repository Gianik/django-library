from django.urls import path
from .api import BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view({
        'get': 'list'

    }), name='book-list')



]
