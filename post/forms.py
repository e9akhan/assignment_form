"""
    Module name :- forms.
"""

from django import forms
from post.models import Category, Post


class CategoryForm(forms.ModelForm):
    """
    Category Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Category
        fields = "__all__"

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class PostForm(forms.ModelForm):
    """
    Post Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Post
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
