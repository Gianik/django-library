from rest_framework import serializers
from .models import Books
from users.models import User
from users.serializers import AuthorSerializer


class BookListSerializer(serializers.ModelSerializer):

    # type = serializers.CharField(source='get_type_display')
    # location = serializers.CharField(source='get_location_display')
    # status = serializers.CharField(source='get_status_display')
    author = AuthorSerializer(read_only=True, many=True)
    # author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ['title', 'author']

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['owner'] = instance.owner.first_name + \
    #         ' ' + instance.owner.last_name
    #     response['checked_out_by'] = instance.checked_out_by.first_name + \
    #         ' ' + instance.checked_out_by.last_name

    #     return response


class NewBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['title', 'author', 'status', 'type', 'location', 'owner']
