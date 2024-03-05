"""
    Module name :- forms.
"""

from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    """
    BookForm.
    """

    class Meta:
        """
        Meta class.
        """

        model = Book
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
        }
