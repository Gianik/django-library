from django.urls import path
from .views import HomeView
from .api import AuthorChoiceViewSet

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/', AuthorChoiceViewSet.as_view({
        'get': 'list'

    }), name='book-list')


]
