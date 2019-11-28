from django.urls import path
from .views import ListSongsView, SongDetailView, ListUsersView, ListUserSongView, SangASongView, AddRateSangASongView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/<id_song>', SongDetailView.as_view(), name="songs-all"),

    path('users/', ListUsersView.as_view(), name="users-all"),

    path('usersong/', ListUserSongView.as_view(), name="usersong-all"),
    path('songs/<id_song>/sang', SangASongView.as_view(), name="sang-a-song"),

    path('rate/<id_sang_song>', AddRateSangASongView.as_view(), name="rate-song-sang"),
]