from rest_framework import serializers
from .models import User


class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class UserIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']
