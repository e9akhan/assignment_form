"""
    Module name :- apps.
"""

from django.apps import AppConfig


class BooksConfig(AppConfig):
    """
    Class for configuration.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "books"
