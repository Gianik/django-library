from django.urls import path
from .views import HomeView, LoginView, LogoutView
from .api import AuthorChoiceViewSet, UserViewSet

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('authors/', AuthorChoiceViewSet.as_view({
        'get': 'list'

    }), name='book-list'),
    path('login-logout-user/', UserViewSet.as_view({
        'post': 'log_in',
        'get': 'log_out'
    }), name='login-logout-user')



]
