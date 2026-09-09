from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Student, Course, StudentCourse
from .serializer import TeacherSerializer, StudentSerializer, CourseSerializer, StudentCourseSerializer

# --- Vistas de la API (DRF) ---
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

# --- Vistas de la WEB (HTML) ---
def home_view(request):
    return render(request, 'academic/base.html')

def courses_view(request):
    return render(request, 'academic/courses.html')

def students_view(request):
    return render(request, 'academic/students.html')