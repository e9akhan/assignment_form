"""
    Module name :- admin
"""

from django.contrib import admin
from post.models import Post, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
