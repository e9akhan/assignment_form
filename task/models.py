"""
    Module name :- models
"""

from django.db import models


# Create your models here.
class Project(models.Model):
    """
    Project Model.
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        """
        String representation.
        """
        return f"{self.name}"


class Task(models.Model):
    """
    Task Model.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.name} - {self.project}"
