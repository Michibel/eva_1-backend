# academic/serializers.py
# Serializadores para convertir modelos a JSON (y viceversa)
# Usados por Django REST Framework para la API

from rest_framework import serializers
from .models import Teacher, Student, Course, StudentCourse


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Teacher
    Convierte objetos Teacher a JSON y viceversa
    """
    class Meta:
        model = Teacher  # Modelo que se va a serializar
        fields = '__all__'  # Incluye todos los campos del modelo


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Student
    Convierte objetos Student a JSON y viceversa
    """
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Course
    Incluye el nombre del profesor como campo adicional (read_only)
    """
    # Campo adicional que muestra el apellido del profesor
    # source='teacher.last_name' indica que el dato viene del modelo relacionado
    teacher_name = serializers.CharField(source='teacher.last_name', read_only=True)

    class Meta:
        model = Course
        # fields: Especifica qué campos incluir en la respuesta JSON
        fields = ['id', 'name', 'teacher', 'teacher_name']


class StudentCourseSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo StudentCourse (Tabla de inscripciones)
    Convierte objetos StudentCourse a JSON y viceversa
    """
    class Meta:
        model = StudentCourse
        fields = '__all__'