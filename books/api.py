from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import BookListSerializer, BookDetailSerializer, BookUpdateDetailSerializer, BookUpdateSerializer
from .models import Books
from users.models import User
from django.shortcuts import get_object_or_404
from users.serializers import AuthorSerializer
from users.models import User


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

    def retrieve(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        users = User.objects.all()
        serializer2 = AuthorSerializer(users, many=True)
        serializer = BookDetailSerializer(book)

        return JsonResponse(serializer.data, safe=False, status=200)
        # return JsonResponse({'data': serializer.data, 'data2': serializer2.data}, safe=False, status=200)

    def retrieve2(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        users = User.objects.all()
        serializer = BookUpdateDetailSerializer(book)
        serializer2 = AuthorSerializer(users, many=True)
        return JsonResponse({'data': serializer.data, 'data2': serializer2.data}, safe=False, status=200)

    def update(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookUpdateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        article = get_object_or_404(Books, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
