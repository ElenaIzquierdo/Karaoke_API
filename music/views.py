from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Songs, UserSong
from .serializers import SongsSerializer, UserSerializer, UserSongSerializer


class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def get(self, request):
        """ Provides a list of all songs. """
        queryset = Songs.objects.all()
        serializer = SongsSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Creates a new song. """
        serializer = SongsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongsSerializer

    def get(self, request, id_song):
        """ Provides a song by its id. """
        a_song = get_object_or_404(Songs, pk=id_song)
        serializer = SongsSerializer(a_song)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id_song):
        a_song = get_object_or_404(Songs, pk=id_song)
        serializer = SongsSerializer(a_song, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class AddRateSangASongView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSongSerializer
    queryset = UserSong.objects.all()

    def get(self, request, id_sang_song):
        """ Provides a song by its id. """
        a_sang_song = get_object_or_404(UserSong, pk=id_sang_song)
        serializer = UserSongSerializer(a_sang_song)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id_sang_song):
        a_sang_song = get_object_or_404(UserSong, pk=id_sang_song)
        serializer = UserSongSerializer(a_sang_song, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class ListUsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        """ Provides a list of all users. """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Creates a new user. """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class ListUserSongView(generics.ListAPIView):
    queryset = UserSong.objects.all()
    serializer_class = UserSongSerializer

    def get(self, request):
        """ Provides a list of all songs that have been sang. """
        queryset = UserSong.objects.all()
        serializer = UserSongSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SangASongView(generics.CreateAPIView):
    queryset = UserSong.objects.all()
    serializer_class = UserSongSerializer

    def post(self, request, id_song):
        """ Creates a new instance to save who sang each song and the performance's rate. """
        a_song = get_object_or_404(Songs, pk=id_song)
        UserSong.objects.create(user=request.user, song=a_song)
        return Response(status=status.HTTP_201_CREATED)
