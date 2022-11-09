from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import BookListSerializer
from .models import Books


class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = Books.objects.all()
        serializer = BookListSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


# class BookChoicesViewset(viewsets.ViewSet):

#     def list(self,request):
