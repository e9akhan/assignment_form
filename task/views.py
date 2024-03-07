"""
    Module name :- views.
"""

from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponse
from task.forms import ProjectForm, TaskForm


# Create your views here.
class AddTask(FormView):
    """
    Add Task View.
    """

    template_name = "forms/form.html"
    form_class = TaskForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Task added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Task."
        context["header"] = "Add Task"
        context["fk_urls"] = ["project"]
        return context


class AddProject(FormView):
    """
    Add Project View.
    """

    template_name = "forms/form.html"
    form_class = ProjectForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()

        if self.request.GET.get("next", []):
            return redirect(self.request.GET["next"])

        return HttpResponse("Project added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Project"
        context["header"] = "Add Project"
        return context
