"""
    Module name :- models
"""

from django.db import models

# Create your models here.


class Book(models.Model):
    """
    Book Model.
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, help_text="Enter only 13 characters.")

    def __str__(self):
        """
        String Representation.
        """
        return f"{self.title} - {self.author}"
