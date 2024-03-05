"""
    Module name :- forms
"""

from django import forms
from song.models import Song


class SongForm(forms.ModelForm):
    """
    Song Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Song
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.TextInput(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
            "duration": forms.TextInput(attrs={"class": "form-control"}),
        }
