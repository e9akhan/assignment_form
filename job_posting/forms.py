"""
    Module name :- forms.
"""

from django import forms
from job_posting.models import JobPost


class JobPostForm(forms.ModelForm):
    """
    Job Post Form.
    """

    class Meta:
        """
        Meta class.
        """

        model = JobPost
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "employment_type": forms.Select(attrs={"class": "form-select"}),
        }
