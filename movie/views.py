"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from movie.forms import MovieForm


# Create your views here.
def add_movie(request):
    """
    Movie view.
    """
    if request.method == "POST":
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Movie successfully added.")

    form = MovieForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Movie", "header": "Add Movie"},
    )
