"""
    Module name :- views
"""

from django.shortcuts import render
from django.http import HttpResponse
from song.forms import SongForm


# Create your views here.
def add_song(request):
    """
    Song view.
    """
    if request.method == "POST":
        form = SongForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Song successfully added.")

    form = SongForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Song", "header": "Add Song"},
    )
