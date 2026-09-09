# academic/admin.py
# Registro de modelos en el panel administrativo de Django

from django.contrib import admin
from .models import Teacher, Student, Course, StudentCourse

# Registrar cada modelo para que aparezca en el admin
# Esto permite gestionar los datos desde http://127.0.0.1:8000/admin/
admin.site.register(Teacher)        # Registra el modelo Teacher
admin.site.register(Student)        # Registra el modelo Student
admin.site.register(Course)         # Registra el modelo Course
admin.site.register(StudentCourse)  # Registra el modelo StudentCourse