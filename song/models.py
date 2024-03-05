"""
    Module name :- models
"""

from django.db import models


# Create your models here.
class Song(models.Model):
    """
    Song Model.
    """

    genres = [
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Hip Hop", "Hip Hop"),
        ("Electronic", "Electronic"),
    ]
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=15, choices=genres)
    duration = models.FloatField()

    def __str__(self):
        """
        String representation.
        """
        return f"{self.title} - {self.artist}"
