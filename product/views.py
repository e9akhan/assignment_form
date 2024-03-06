"""
    Module name :- views.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.forms import CategoryForm, ProductForm


# Create your views here.
def add_product_category(request):
    """
    Add product category view.
    """
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            if request.GET.get("next", []):
                return redirect(request.GET["next"])

            return HttpResponse("Category added.")

    form = CategoryForm()
    return render(
        request,
        "forms/form.html",
        {"form": form, "title": "Add Category", "header": "Add Category"},
    )


def add_product(request):
    """
    Add product view.
    """
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Product successfully added.")

    form = ProductForm()
    return render(
        request,
        "forms/form.html",
        {
            "form": form,
            "title": "Add Product",
            "header": "Add Product",
            "fk_urls": ["product_category"],
        },
    )
