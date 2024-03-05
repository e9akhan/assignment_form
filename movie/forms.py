"""
    Module name :- forms.
"""

from django import forms
from movie.models import Movie


class MovieForm(forms.ModelForm):
    """
    Movie Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Movie
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "director": forms.TextInput(attrs={"class": "form-control"}),
            "release_year": forms.NumberInput(attrs={"class": "form-control"}),
            "rating": forms.Select(attrs={"class": "form-select"}),
        }
