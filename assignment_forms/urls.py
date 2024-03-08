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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


from books.views import AddBookView, home
from car.views import AddCarView
from song.views import AddSong
from movie.views import AddMovie
from job_posting.views import AddJobPost
from product.views import AddProduct, AddProductCategory
from task.views import AddTask, AddProject
from post.views import AddPost, AddPostCategory
from enrollment.views import AddStudent, AddCourse, Enrollment

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("book/", AddBookView.as_view(), name="book"),
    path("car/", AddCarView.as_view(), name="car"),
    path("song/", AddSong.as_view(), name="song"),
    path("movie/", AddMovie.as_view(), name="movie"),
    path("job/", AddJobPost.as_view(), name="job"),
    path("product/", AddProduct.as_view(), name="product"),
    path("product/category/", AddProductCategory.as_view(), name="product_category"),
    path("task/", AddTask.as_view()),
    path("project/", AddProject.as_view(), name="project"),
    path("post/", AddPost.as_view()),
    path("post/category/", AddPostCategory.as_view(), name="post_category"),
    path("student/", AddStudent.as_view(), name="student"),
    path("course/", AddCourse.as_view(), name="course"),
    path("enrollment/", Enrollment.as_view()),
    path("api/v1/", include("api.urls")),
    path("api-auth", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token),
]
