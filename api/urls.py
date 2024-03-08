"""
    Module name :- urls
"""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from api.views import (
    BookListCreate,
    BookDetail,
    CarList,
    CarDetail,
    StudentList,
    StudentDetail,
    CourseList,
    CourseDetail,
    EnrollmentList,
    EnrollmentDetail,
    JobPostList,
    JobPostDetail,
    MovieList,
    MovieDetail,
    PostList,
    PostDetail,
    SongList,
    SongDetail,
    ProductList,
    ProductDetail,
    TaskList,
    TaskDetail,
    ProjectList,
    ProjectDetail,
)

urlpatterns = [
    path("books/", BookListCreate.as_view(), name="book-list"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book-detail"),
    path("cars/", CarList.as_view(), name="car-list"),
    path("car/<int:pk>/", CarDetail.as_view(), name="car-detail"),
    path("students/", StudentList.as_view(), name="student-list"),
    path("student/<int:pk>/", StudentDetail.as_view(), name="student-detail"),
    path("courses/", CourseList.as_view(), name="course-list"),
    path("course/<int:pk>/", CourseDetail.as_view(), name="course-detail"),
    path("enrollments/", EnrollmentList.as_view(), name="enrollment-list"),
    path("enrollment/<int:pk>/", EnrollmentDetail.as_view(), name="enrollment-detail"),
    path("jobs/", JobPostList.as_view(), name="job-list"),
    path("job/<int:pk>/", JobPostDetail.as_view(), name="job-detail"),
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movie/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
    path("posts/", PostList.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("products/", ProductList.as_view(), name="product-list"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("songs/", SongList.as_view(), name="song-list"),
    path("song/<int:pk>/", SongDetail.as_view(), name="song-detail"),
    path("tasks/", TaskList.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
    path("projects/", ProjectList.as_view(), name="project-list"),
    path("project/<int:pk>/", ProjectDetail.as_view(), name="project-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
