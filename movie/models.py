"""
    Module name :- models
"""

from django.db import models


# Create your models here.
class Movie(models.Model):
    """
    Movie Model.
    """

    ratings = [
        ("G", "G"),
        ("H", "H"),
        ("I", "I"),
        ("J", "J"),
        ("K", "K"),
        ("L", "L"),
        ("M", "M"),
        ("N", "N"),
        ("O", "O"),
        ("P", "P"),
        ("Q", "Q"),
        ("R", "R"),
    ]

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=1, choices=ratings)

    def __str__(self):
        """
        String representation
        """
        return f"{self.title} - {self.director}"
