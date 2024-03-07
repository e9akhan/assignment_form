"""
    Module name :- views.
"""

from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponse
from product.forms import CategoryForm, ProductForm


# Create your views here.
class AddProductCategory(FormView):
    """
    Add Product Category View.
    """

    template_name = "forms/form.html"
    form_class = CategoryForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()

        if self.request.GET.get("next", []):
            return redirect(self.request.GET["next"])

        return HttpResponse("Category added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Category"
        context["header"] = "Add Category"
        return context


class AddProduct(FormView):
    """
    Add Product View
    """

    template_name = "forms/form.html"
    form_class = ProductForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Product successfully added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Product"
        context["header"] = "Add Product"
        context["fk_urls"] = ["product_category"]
        return context
