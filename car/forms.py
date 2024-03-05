"""
    Module name :- forms
"""

from django import forms
from car.models import Car


class CarForm(forms.ModelForm):
    """
    Car Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = Car
        fields = "__all__"

        widgets = {
            "make": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "transmission": forms.RadioSelect(),
        }
