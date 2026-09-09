# academic/views.py
# Vistas del proyecto con todas las páginas

from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Student, Course, StudentCourse
from .serializers import (
    TeacherSerializer, 
    StudentSerializer, 
    CourseSerializer, 
    StudentCourseSerializer
)

# ============================================
# VISTAS DE LA API (Django REST Framework)
# ============================================

class TeacherViewSet(viewsets.ModelViewSet):
    """CRUD completo para profesores"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD completo para estudiantes"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """CRUD completo para cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentCourseViewSet(viewsets.ModelViewSet):
    """CRUD completo para inscripciones"""
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer


# ============================================
# VISTAS DE LA WEB (HTML)
# ============================================

def home_view(request):
    """Página de inicio"""
    return render(request, 'academic/base.html')


def teachers_view(request):
    """Página de gestión de profesores con CRUD"""
    return render(request, 'academic/teachers.html')


def courses_view(request):
    """Página de gestión de cursos con CRUD"""
    return render(request, 'academic/courses.html')


def students_view(request):
    """Página de gestión de estudiantes con CRUD"""
    return render(request, 'academic/students.html')