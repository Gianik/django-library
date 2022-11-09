from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import BookListSerializer
from .models import Books
from users.models import User
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = Books.objects.all()
        serializer = BookListSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    def create(self, request):
        serializer = BookListSerializer(data=request.data)
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=request.POST['owner'])
        authors = queryset.filter(id__in=request.POST.getlist('author[]'))

        if serializer.is_valid():
            serializer.owner = user
            serializer.save(owner=user, author=authors)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookChoicesViewset(viewsets.ViewSet):

#     def list(self,request):
