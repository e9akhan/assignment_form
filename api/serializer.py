"""
    Module name :- serializer
"""

from rest_framework import serializers

from books.models import Book
from car.models import Car
from enrollment.models import Student, Course, Enrollment
from job_posting.models import JobPost
from movie.models import Movie
from post.models import Post
from product.models import Product
from song.models import Song
from task.models import Task, Project


class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    Book Serializer class.
    """

    class Meta:
        """
        Meta class.
        """

        model = Book
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class CarSerializer(serializers.HyperlinkedModelSerializer):
    """
    Car Serializer class.
    """

    class Meta:
        """
        Meta class
        """

        model = Car
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    Enrollment Serializer class.
    """

    url = serializers.HyperlinkedIdentityField(view_name="enrollment-detail")
    student_desc = serializers.SerializerMethodField()
    course_desc = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class.
        """

        model = Enrollment
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "student": {"write_only": True},
            "course": {"write_only": True},
        }

    def get_course_desc(self, obj):
        """
        Course description.
        """
        return CourseSerializer(obj.course).data

    def get_student_desc(self, obj):
        """
        Student description.
        """
        return StudentSerializer(obj.student).data


class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer class.
    """

    class Meta:
        """
        Meta class.
        """

        model = Student
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class CourseSerializer(serializers.ModelSerializer):
    """
    Course Serializer class.
    """

    class Meta:
        """
        Meta class.
        """

        model = Course
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class JobPostSerializer(serializers.ModelSerializer):
    """
    Job Post Serializer.
    """

    url = serializers.HyperlinkedIdentityField(view_name="job-detail")

    class Meta:
        """
        Meta class.
        """

        model = JobPost
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    Movie Serializer.
    """

    class Meta:
        """
        Meta class.
        """

        model = Movie
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    url = serializers.HyperlinkedIdentityField(view_name="post-detail")

    class Meta:
        """
        Meta class.
        """

        model = Post
        fields = "__all__"
        extra_kwargs = {"category": {"write_only": True}, "id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    """
    Product Serializer.
    """

    url = serializers.HyperlinkedIdentityField(view_name="product-detail")

    class Meta:
        """
        Meta class.
        """

        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}, "category": {"write_only": True}}


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Song Serializer.
    """

    class Meta:
        """
        Meta class.
        """

        model = Song
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class TaskSerializer(serializers.ModelSerializer):
    """
    Task Serializer.
    """

    project_desc = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="task-detail")

    class Meta:
        """
        Meta class.
        """

        model = Task
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}, "project": {"write_only": True}}

    def get_project_desc(self, obj):
        """
        Project description.
        """
        return ProjectSerializer(obj.project).data


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project Serializer.
    """

    class Meta:
        """
        Meta class.
        """

        model = Project
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
