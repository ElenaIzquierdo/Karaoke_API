from django.contrib.auth.models import User
from django.db import models


class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)

class UserSong(models.Model):
    RATE_CHOICES = (
        (5, "REALLY GOOD"),
        (4, "GOOD"),
        (3, "NOT REALLY GOOD"),
        (2, "BAD"),
        (1, "REALLY BAD"),
    )
    # song_id song that was sang
    song = models.ForeignKey(Songs, null=False, on_delete=models.CASCADE)

    # user_id user who sang the song
    user = models.ForeignKey(User, null = False, on_delete=models.CASCADE)

    #rate how the user sang the song
    rate = models.IntegerField(choices= RATE_CHOICES, null = True, blank=True)

    def __str__(self):
        return "{} - {}: {}".format(self.song, self.user, self.rate)