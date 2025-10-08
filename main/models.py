from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#App has two roles (Student,Teachers)
#Modify User model to have two roles.
class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
    role = models.CharField(
        choices=Role,
        max_length=20,
        default=None,
        null=True
    )
    def _is_student(self):
        return self.role == self.Role.STUDENT
    def _is_teacher(self):
        return self.role == self.Role.TEACHER




class Course(models.Model):
    course_name = models.CharField(max_length=100)

    # One teacher per course
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'TEACHER'},  # only teachers
        related_name="courses_uploaded"
    )

    # Many students can register for a course
    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="registered_courses",
        blank=True,
        null=True,
        limit_choices_to={'role': 'STUDENT'},
        default=None  # only students
    )

    file = models.FileField(upload_to="courses/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name


    def __str__(self):
        return self.course_name


