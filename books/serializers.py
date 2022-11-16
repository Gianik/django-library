from rest_framework import serializers
from .models import Books, Comments, Authors
from users.serializers import AuthorSerializer
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = ['author']


class CommentsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text', 'author', 'date_updated']


class NewCommentSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ['author', 'text', 'book']


class BookListSerializer(serializers.ModelSerializer):

    author_tags = AuthorsSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Books
        fields = ['id', 'title', 'author_tags']


class NewBookSerializer(serializers.ModelSerializer):
    author_tags = AuthorsSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Books
        fields = ['title', 'status',
                  'type', 'location', 'owner', 'author_tags']


class BookDetailSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    location = serializers.CharField(source='get_location_display')
    status = serializers.CharField(source='get_status_display')
    author_tags = AuthorsSerializer(read_only=True, many=True, required=False)
    comments = CommentsSerializer(read_only=True, many=True)

    class Meta:
        model = Books
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['owner'] = instance.owner.first_name + \
            ' ' + instance.owner.last_name
        if (response['checked_out_by'] is not None):
            response['checked_out_by'] = instance.checked_out_by.first_name + \
                ' ' + instance.checked_out_by.last_name

        return response


class BookUpdateDetailSerializer(serializers.ModelSerializer):
    author_tags = AuthorsSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Books
        fields = '__all__'


class BookUpdateSerializer(serializers.ModelSerializer):
    author_tags = AuthorsSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Books
        fields = ['title', 'owner',
                  'checked_out_by', 'status', 'type', 'location', 'author_tags']


class BookDeleteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'title']
