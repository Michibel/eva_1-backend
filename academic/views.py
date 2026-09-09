# academic/views.py
# Vistas del proyecto: API (DRF) y Web (HTML)

from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Student, Course, StudentCourse
from .serializer import (
    TeacherSerializer, 
    StudentSerializer, 
    CourseSerializer, 
    StudentCourseSerializer
)

# ============================================
# VISTAS DE LA API (Django REST Framework)
# ============================================

class TeacherViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Teacher
    Proporciona endpoints CRUD para profesores
    Endpoints generados:
        - GET /api/teachers/         -> Lista todos los profesores
        - POST /api/teachers/        -> Crea un nuevo profesor
        - GET /api/teachers/{id}/    -> Obtiene un profesor específico
        - PUT /api/teachers/{id}/    -> Actualiza un profesor
        - DELETE /api/teachers/{id}/ -> Elimina un profesor
    """
    queryset = Teacher.objects.all()  # Consulta a la base de datos
    serializer_class = TeacherSerializer  # Serializador a usar


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Student
    Proporciona endpoints CRUD para estudiantes
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Course
    Proporciona endpoints CRUD para cursos
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentCourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo StudentCourse
    Proporciona endpoints CRUD para inscripciones
    """
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer


# ============================================
# VISTAS DE LA WEB (HTML)
# ============================================

def home_view(request):
    """
    Vista para la página de inicio (home)
    Renderiza la plantilla base con el menú de navegación
    URL: /
    """
    return render(request, 'academic/base.html')


def courses_view(request):
    """
    Vista para la página de cursos
    Renderiza la plantilla que muestra la lista de cursos
    URL: /courses/
    """
    return render(request, 'academic/courses.html')


def students_view(request):
    """
    Vista para la página de estudiantes
    Renderiza la plantilla que muestra la lista de estudiantes
    URL: /students/
    """
    return render(request, 'academic/students.html')