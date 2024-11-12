# music_lyrics/models.py

from django.db import models
from django.utils import timezone


class Lyrics(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    lyrics = models.TextField()
    visit_count = models.PositiveIntegerField(default=0)  # Track visits
    date_added = models.DateTimeField(default=timezone.now)  # Track addition date



    def __str__(self):
        return f"{self.title} by {self.artist}"