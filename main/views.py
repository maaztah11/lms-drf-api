from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import *
from .permissions import IsTeacher, IsStaffUser  # your custom permission
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
# myapp/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsStaffUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsStaffUser])
def user_counts(request):
    teacher_count = User.objects.filter(role="TEACHER").count()
    student_count = User.objects.filter(role="STUDENT").count()
    return Response({
        "teachers": teacher_count,
        "students": student_count
    })
@api_view(["GET"])
@permission_classes([IsStaffUser])
def custom_admin_dashboard(request):
    """
    Custom admin dashboard endpoint.
    Only staff users can access this.
    """
    teachers = TeacherProfile.objects.all()
    students = StudentProfile.objects.all()
    teacher_data = TeacherProfileSerializer(teachers, many=True).data
    student_data = StudentProfileSerializer(students, many=True).data

    return Response({
        "message": "Welcome to the custom admin dashboard!",
        "user": request.user.username,
        "is_staff": request.user.is_staff,
        "teachers": teacher_data,
        "students": student_data
    })





class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacher]
class UserSignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)