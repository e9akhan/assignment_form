"""
    Module name :- forms
"""

from django import forms
from product.models import Category, Product


class CategoryForm(forms.ModelForm):
    """
    Category Form
    """

    class Meta:
        """
        Meta class.
        """

        model = Category
        fields = "__all__"

        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class ProductForm(forms.ModelForm):
    """
    Product Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Product
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
