"""
URL configuration for assignment_forms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from books.views import AddBookView
from car.views import add_car
from song.views import add_song
from movie.views import add_movie
from job_posting.views import add_job
from product.views import add_product, add_product_category
from task.views import add_task, add_project
from post.views import add_post, add_post_category
from enrollment.views import add_course, add_student, add_enrollment

urlpatterns = [
    path("admin/", admin.site.urls),
    path("book/", AddBookView.as_view(), name="book"),
    path("car/", add_car, name="car"),
    path("song/", add_song, name="song"),
    path("movie/", add_movie, name="movie"),
    path("job/", add_job, name="job"),
    path("product/", add_product, name="product"),
    path("product/category/", add_product_category),
    path("task/", add_task),
    path("project/", add_project),
    path("post/", add_post),
    path("post/category/", add_post_category),
    path("student/", add_student),
    path("course/", add_course),
    path("enrollment/", add_enrollment),
]
