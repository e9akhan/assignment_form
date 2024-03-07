"""
    Module name :- views.
"""

from django.shortcuts import redirect
from django.views.generic import FormView
from django.http import HttpResponse
from post.forms import CategoryForm, PostForm


# Create your views here.
class AddPostCategory(FormView):
    """
    Post Category View.
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

        return HttpResponse("Category successfully added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Category"
        context["header"] = "Add Category"
        return context


class AddPost(FormView):
    """
    Post View.
    """

    template_name = "forms/form.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        Form valid.
        """
        form.save()
        return HttpResponse("Post added.")

    def get_context_data(self, **kwargs):
        """
        get_context_data.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Post"
        context["header"] = "Add Post"
        context["fk_urls"] = ["post_category"]
        return context
