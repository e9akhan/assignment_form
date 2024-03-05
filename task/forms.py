"""
    Module name :- forms
"""

from django import forms
from task.models import Task, Project


class ProjectForm(forms.ModelForm):
    """
    Project Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Project
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }


class TaskForm(forms.ModelForm):
    """
    Task Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Task
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "project": forms.Select(attrs={"class": "form-select"}),
        }
