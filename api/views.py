"""
    Module name :- views
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import Book
from car.models import Car
from enrollment.models import Student, Course, Enrollment
from job_posting.models import JobPost
from movie.models import Movie
from post.models import Post
from product.models import Product
from song.models import Song
from task.models import Task, Project

from api.serializer import (
    BookSerializer,
    CarSerializer,
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    JobPostSerializer,
    MovieSerializer,
    PostSerializer,
    ProductSerializer,
    SongSerializer,
    TaskSerializer,
    ProjectSerializer,
)

# Create your views here.


class BookListCreate(ListCreateAPIView):
    """
    Book List Create View.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetail(RetrieveUpdateDestroyAPIView):
    """
    Book Detail View.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CarList(ListCreateAPIView):
    """
    Car List Create View.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CarDetail(RetrieveUpdateDestroyAPIView):
    """
    Car Detail View.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = SessionAuthentication, TokenAuthentication
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentList(ListCreateAPIView):
    """
    Student List View.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class StudentDetail(RetrieveUpdateDestroyAPIView):
    """
    Student Detail View.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseList(ListCreateAPIView):
    """
    Course List.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CourseDetail(RetrieveUpdateDestroyAPIView):
    """
    Course Detail
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnrollmentList(ListCreateAPIView):
    """
    Enrollment List.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnrollmentDetail(RetrieveUpdateDestroyAPIView):
    """
    Enrollment Detail.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class JobPostList(ListCreateAPIView):
    """
    Job Post List.
    """

    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class JobPostDetail(RetrieveUpdateDestroyAPIView):
    """
    Job Post Detail.
    """

    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieList(ListCreateAPIView):
    """
    Movie List.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieDetail(RetrieveUpdateDestroyAPIView):
    """
    Movie Detail.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostList(ListCreateAPIView):
    """
    Post List View.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    Post Detail View.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductList(ListCreateAPIView):
    """
    Product List View.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """
    Product Detail View.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongList(ListCreateAPIView):
    """
    Song List View.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongDetail(RetrieveUpdateDestroyAPIView):
    """
    Song Detail View.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskList(ListCreateAPIView):
    """
    Task List View.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class TaskDetail(RetrieveUpdateDestroyAPIView):
    """
    Task Detail View.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectList(ListCreateAPIView):
    """
    Project List View.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    """
    Project Detail View.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = SessionAuthentication, TokenAuthentication
    permission_classes = [IsAuthenticatedOrReadOnly]
