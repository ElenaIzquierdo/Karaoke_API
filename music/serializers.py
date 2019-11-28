from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Songs, UserSong


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")


class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSong
        fields = ("user", "song", "rate")

