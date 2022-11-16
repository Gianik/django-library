from django.urls import path
from .views import HomeView, LoginView, LogoutView, RegisterView, DashboardView, EditProfileView
from .api import AuthorChoiceViewSet, UserViewSet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', EditProfileView.as_view(), name='profile'),
    path('authors/', AuthorChoiceViewSet.as_view({
        'get': 'list'
    }), name='book-list'),
    path('login-logout-user/', UserViewSet.as_view({
        'post': 'log_in',
        'get': 'log_out'
    }), name='login-logout-user'),
    path('register-user/', UserViewSet.as_view({
        'post': 'user_register'
    }), name='register-user'),
    path('detail/', UserViewSet.as_view({
        'get': 'user_details'
    }), name='book-list'),
    path('profile-details/', UserViewSet.as_view({
        'get': 'profile_details',
        'post': 'update_profile'
    }), name='profile-detail'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
