from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import AuthorSerializer, UserRegistrationSerializer, UserDetailsSerializer, UserProfileSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password


class AuthorChoiceViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        serializer = AuthorSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


class UserViewSet(viewsets.ViewSet):

    def user_register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        password = make_password(request.POST['password'])
        if serializer.is_valid():
            serializer.save(password=password)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def log_in(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response('successful login')
        else:
            return Response(status=404)

    def log_out(self, request):

        logout(request)
        return Response('successful logout')

    def user_details(self, request):
        serializer = UserDetailsSerializer(request.user)
        return JsonResponse(serializer.data, safe=False, status=200)

    def profile_details(self, request):
        serializer = UserProfileSerializer(request.user)
        return JsonResponse(serializer.data, safe=False, status=200)

    def update_profile(self, request):
        user = get_object_or_404(User, pk=request.user.id)

        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
