"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from car.forms import CarForm


# Create your views here.
def add_car(request):
    """
    Add car view.
    """
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Car successfully created.")

    form = CarForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Car", "header": "Add Car"},
    )
