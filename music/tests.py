from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer, UserSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    @staticmethod
    def create_user(first_name="", last_name="", username="", email=""):
        if first_name != "" and last_name != "" and username != "" and email != "":
            User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)

    def setUp(self):
        # add test data for songs
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

        #add test data for users
        self.create_user("Elena", "Izquierdo", "eizquierdo", "e@gmail.com")
        self.create_user("Ola", "Zyoto", "olaola", "ola@gmail.com")
        self.create_user("Irene", "Cabezas", "icabezas", "icbzs@gmail.com")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all")
        )
        # fetch the data from db
        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_song_from_id(self):
        """
        This test ensures that the first song added in the setUp method
        exist when we make a GET request to the songs/id endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"id_song": "1"})
        )
        # fetch the data from db
        expected = Songs.objects.get(id=1)
        serialized = SongsSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllUsersTest(BaseViewTest):

    def test_get_all_users(self):
        """
        This test ensures that all users added in the setUp method
        exist when we make a GET request to the users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("users-all")
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


