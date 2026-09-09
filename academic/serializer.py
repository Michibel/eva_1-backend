# academic/serializers.py

from rest_framework import serializers
from .models import Teacher, Student, Course, StudentCourse


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher.last_name', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']


class StudentSerializer(serializers.ModelSerializer):
    # Campo adicional para mostrar cursos del estudiante
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'courses']

    def get_courses(self, obj):
        """Obtiene los cursos del estudiante"""
        enrollments = obj.courses.all()  # related_name='courses' en StudentCourse
        return [enrollment.course.name for enrollment in enrollments]


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'