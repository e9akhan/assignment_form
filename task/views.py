"""
    Module name :- views.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from task.forms import ProjectForm, TaskForm


# Create your views here.
def add_task(request):
    """
    Add task view.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Task added.")

    form = TaskForm()
    return render(
        request,
        "forms/form.html",
        {
            "form": form,
            "title": "Add Task",
            "header": "Add Task",
            "fk_urls": ["project"],
        },
    )


def add_project(request):
    """
    Add project view.
    """
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()

            if request.GET.get("next", []):
                return redirect(request.GET["next"])

            return HttpResponse("Project added.")

    form = ProjectForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Project", "header": "Add Project"},
    )
