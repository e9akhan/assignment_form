"""
    Module name :- views.
"""

from django.views.generic import FormView
from django.http import HttpResponse
from job_posting.forms import JobPostForm


# Create your views here.
class AddJobPost(FormView):
    """
    Add Job Post View.
    """

    template_name = "forms/form.html"
    form_class = JobPostForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Job successfully posted.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Post a Job"
        context["header"] = "Create a Job Post"
        return context
