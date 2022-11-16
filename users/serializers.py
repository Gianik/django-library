from rest_framework import serializers
from .models import User
from django.conf import settings
from books.models import Books
# from books.serializers import BookUserListSerializer


class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class BookUserListSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Books
        fields = ['id', 'title', 'author']


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", 'first_name', 'last_name', "password"]


class UserDetailsSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    book_owner = BookUserListSerializer(read_only=True, many=True)
    book_borrower = BookUserListSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'avatar',
                  'book_owner', 'book_borrower']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']
