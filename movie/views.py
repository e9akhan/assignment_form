"""
    Module name :- views.
"""

from django.views.generic import FormView
from django.http import HttpResponse
from movie.forms import MovieForm


# Create your views here.
class AddMovie(FormView):
    """
    Add Movie View.
    """

    template_name = "forms/form.html"
    form_class = MovieForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Movie successfully added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Movie"
        context["header"] = "Add Movie"
        return context
