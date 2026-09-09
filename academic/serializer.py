from rest_framework import serializers
from .models import Teacher, Student, Course, StudentCourse

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    # Incluimos el nombre del profesor en la respuesta para que sea más amigable
    teacher_name = serializers.CharField(source='teacher.last_name', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']

class StudentCourseSerializer(serializers.ModelSerializer):
    # Podemos anidar la información del estudiante y curso si quisiéramos, pero para este proyecto lo dejamos simple.
    class Meta:
        model = StudentCourse
        fields = '__all__'  