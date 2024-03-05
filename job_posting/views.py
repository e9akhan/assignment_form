"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from job_posting.forms import JobPostForm


# Create your views here.
def add_job(request):
    """
    Job Post view.
    """
    if request.method == "POST":
        form = JobPostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Job successfully posted.")

    form = JobPostForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Post a Job", "header": "Create a Job Post"},
    )
