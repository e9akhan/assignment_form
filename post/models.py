"""
    Module name :- models
"""

from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Category Model.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.name}"


class Post(models.Model):
    """
    Post Model.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.title} - {self.category}"
