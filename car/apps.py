"""
    Module name :- apps
"""

from django.apps import AppConfig


class CarConfig(AppConfig):
    """
    Class for app config.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "car"
