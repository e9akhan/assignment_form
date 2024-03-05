"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from books.forms import BookForm


# Create your views here.
def add_book(request):
    """
    Add Book View.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book successfully created")
    form = BookForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Book", "header": "Add Book"},
    )
