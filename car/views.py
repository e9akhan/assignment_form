"""
    Module name :- views.
"""

from django.views.generic import FormView
from django.http import HttpResponse
from car.forms import CarForm


# Create your views here.
class AddCarView(FormView):
    """
    Add Car View
    """

    template_name = "forms/form.html"
    form_class = CarForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Car successfully added.")

    def get_context_data(self, **kwargs):
        """
        Get context data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Car"
        context["header"] = "Add Car"
        return context
