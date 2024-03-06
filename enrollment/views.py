"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from enrollment.forms import StudentForm, CourseForm, EnrollmentForm


# Create your views here.
def add_student(request):
    """
    Add student view.
    """
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Student added.")

    form = StudentForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Student", "header": "Add Student"},
    )


def add_course(request):
    """
    Add course view.
    """
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Course added.")

    form = CourseForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Course", "header": "Add Course"},
    )


def add_enrollment(request):
    """
    Add enrollment view.
    """
    if request.method == "POST":
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Enrollment added.")

    form = EnrollmentForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Enrollment", "header": "Enroll a Student"},
    )
