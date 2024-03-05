"""
    Module name :- models.
"""

from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Student Model.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.name}"


class Course(models.Model):
    """
    Course Model.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """
        String representation.
        """
        return f"{self.name}"


class Enrollment(models.Model):
    """
    Enrollment Model.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student} - {self.course}"
