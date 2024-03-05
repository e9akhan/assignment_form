"""
    Module name :- admin
"""

from django.contrib import admin
from job_posting.models import JobPost

# Register your models here.
admin.site.register(JobPost)
