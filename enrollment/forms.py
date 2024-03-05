"""
    Module name :- forms
"""

from django import forms
from enrollment.models import Student, Course, Enrollment


class StudentForm(forms.ModelForm):
    """
    Student Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Student
        fields = "__all__"

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class CourseForm(forms.ModelForm):
    """
    Course Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Course
        fields = "__all__"

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class EnrollmentForm(forms.ModelForm):
    """
    Enrollment Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Enrollment
        fields = "__all__"

        widgets = {
            "student": forms.Select(attrs={"class": "form-select"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "grade": forms.TextInput(attrs={"class": "form-control"}),
        }
