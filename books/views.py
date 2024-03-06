"""
    Module name :- views.
"""

from django.views.generic import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from books.forms import BookForm


# Create your views here.
def home(request):
    """
    Homepage.
    """
    return render(request, "forms/homepage.html")


class AddBookView(CreateView):
    """
    Add Book View.
    """

    template_name = "forms/form.html"
    form_class = BookForm

    def form_valid(self, form):
        form.save()
        return HttpResponse("Book successfully added.")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Book"
        context["header"] = "Add Book"
        return context
