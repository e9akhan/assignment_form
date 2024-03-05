"""
    Module name :- models.
"""

from django.db import models


# Create your models here.
class Car(models.Model):
    """
    Car Model
    """

    transmissions = [("Manual", "Manual"), ("Automatic", "Automatic")]
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.CharField(
        max_length=20, choices=transmissions, default="Manual"
    )

    def __str__(self):
        """
        String representation.
        """
        return f"{self.make} - {self.model}"
