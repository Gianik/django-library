from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import BookListSerializer, BookDetailSerializer, BookUpdateDetailSerializer, BookUpdateSerializer, NewBookSerializer, NewCommentSerializer, CommentsSerializer
from .models import Books, Comments, Authors
from users.models import User
from django.shortcuts import get_object_or_404
from users.serializers import AuthorSerializer
from users.models import User
import json


class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = Books.objects.all()
        serializer = BookListSerializer(books, many=True)
        # user = UserIdSerializer(request.user) test for passing userid along with the json data
        return JsonResponse(serializer.data, safe=False, status=200)

    def create(self, request):
        auth = []
        serializer = NewBookSerializer(data=request.data)
        queryset = User.objects.all()
        authors = queryset.filter(id__in=request.POST.getlist('author[]'))
        tags = request.POST.getlist('author_tags[]')
        # loop to create the authors tag object if it does not exist yet
        for tag in tags:
            if not Authors.objects.filter(author=tag).exists():
                Authors.objects.create(author=tag)
        # loop to get the id of the authors object
        for tag in tags:
            auth_object = Authors.objects.get(author=tag)
            auth.append(auth_object)

        if serializer.is_valid():
            serializer.save(owner=request.user, author_tags=auth)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        user = AuthorSerializer(request.user)
        serializer = BookDetailSerializer(book)
        return JsonResponse({'data': serializer.data, 'data2': user.data}, safe=False, status=200)

    def retrieve2(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        users = User.objects.all()
        serializer = BookUpdateDetailSerializer(book)
        serializer2 = AuthorSerializer(users, many=True)
        return JsonResponse({'data': serializer.data, 'data2': serializer2.data}, safe=False, status=200)

    def retrieve3(self, request, pk=None):
        book = get_object_or_404(Books, pk=pk)
        serializer = BookDetailSerializer(book)
        return JsonResponse(serializer.data, safe=False, status=200)

    def update(self, request, pk=None):
        auth = []
        book = get_object_or_404(Books, pk=pk)
        serializer = BookUpdateSerializer(book, data=request.data)
        tags = request.POST.getlist('author_tags[]')
        # loop to create the authors tag object if it does not exist yet
        for tag in tags:
            if not Authors.objects.filter(author=tag).exists():
                Authors.objects.create(author=tag)
        # loop to get the id of the authors object
        for tag in tags:
            auth_object = Authors.objects.get(author=tag)
            auth.append(auth_object)

        if serializer.is_valid():
            serializer.save(author_tags=auth)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = get_object_or_404(Books, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentsViewSet(viewsets.ViewSet):

    def create(self, request, pk=None):
        serializer = NewCommentSerializer(data=request.data)
        books = get_object_or_404(Books, pk=request.POST['book'])
        if serializer.is_valid():
            serializer.save(book=books, author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        users = User.objects.all()
        serializer = CommentsSerializer(comment)
        return JsonResponse(serializer.data, safe=False, status=200)

    # consider retrieve2 for after delete redirect

    def update(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comments, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
