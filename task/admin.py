"""
    Module name :- admin
"""

from django.contrib import admin
from task.models import Task, Project

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
