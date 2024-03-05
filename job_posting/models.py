"""
    Module name :- models
"""

from django.db import models


# Create your models here.
class JobPost(models.Model):
    """
    Job post Model.
    """

    employment_types = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=employment_types)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.title} - {self.company}"
