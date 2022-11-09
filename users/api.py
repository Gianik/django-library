from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import AuthorSerializer
from .models import User


class AuthorChoiceViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        serializer = AuthorSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
