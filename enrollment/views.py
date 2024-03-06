"""
    Module name :- views.
"""

from django.views.generic import FormView
from django.http import HttpResponse
from django.shortcuts import redirect
from enrollment.forms import StudentForm, CourseForm, EnrollmentForm


# Create your views here.
class AddStudent(FormView):
    """
    Add Student View.
    """

    template_name = "forms/form.html"
    form_class = StudentForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()

        if self.request.GET.get("next", []):
            return redirect(self.request.GET["next"])

        return HttpResponse("Student added.")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Student"
        context["header"] = "Add Student"
        return context


class AddCourse(FormView):
    """
    Add Course View.
    """

    template_name = "forms/form.html"
    form_class = CourseForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()

        if self.request.GET.get("next", []):
            return redirect(self.request.GET["next"])

        return HttpResponse("Course added.")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Course"
        context["header"] = "Add Course"
        return context


class Enrollment(FormView):
    """
    Enrollment.
    """

    template_name = "forms/form.html"
    form_class = EnrollmentForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Enrolled.")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """

        context = super().get_context_data(**kwargs)
        context["title"] = "Enroll"
        context["header"] = "Enroll"
        context["fk_urls"] = ["student", "course"]
        return context
