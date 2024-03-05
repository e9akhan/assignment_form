"""
    Module name :- views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from post.forms import CategoryForm, PostForm


# Create your views here.
def add_post_category(request):
    """
    Add Post Category view.
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Category Added.")

    form = CategoryForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Category", "header": "Add Category"},
    )


def add_post(request):
    """
    Post view.
    """
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Post added.")

    form = PostForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Post", "header": "Add Post"},
    )
