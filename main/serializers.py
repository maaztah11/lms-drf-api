from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims to the token payload
        token['role'] = user.role
        token['username'] = user.username  
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # also return role in the response body
        data['role'] = self.user.role
        return data







class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'file', 'students', 'date_added']
        read_only_fields = ['teacher', 'students']
    def create(self, validated_data):
            course = Course.objects.create(
                teacher=self.context['request'].user,
                **validated_data
            )
            return course

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user