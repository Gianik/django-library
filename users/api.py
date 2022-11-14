from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import AuthorSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout


class AuthorChoiceViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        serializer = AuthorSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


class UserViewSet(viewsets.ViewSet):

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
