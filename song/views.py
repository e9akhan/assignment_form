"""
    Module name :- views
"""

from django.views.generic import FormView
from django.http import HttpResponse
from song.forms import SongForm


# Create your views here.
class AddSong(FormView):
    """
    Add Song View.
    """

    template_name = "forms/form.html"
    form_class = SongForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Song successfully added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Song"
        context["header"] = "Add Song"
        return context
