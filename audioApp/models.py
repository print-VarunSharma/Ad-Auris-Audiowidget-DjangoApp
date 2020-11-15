from django.db import models

# Create your models here.
from django.conf import settings

class Playlist(models.Model):
    author = models.CharField(max_length=250)
    playlist_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.playlist_title + ' - ' + self.author

class Narration(models.Model):
    file = models.FileField(upload_to='media/',default=None)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    narration_title = models.CharField(max_length=250)
    total_narration_time = models.CharField(max_length=250, default=None)

    def __str__(self):
        return self.narration_title
