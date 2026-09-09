# academic/urls.py
# Configuración de URLs para la aplicación academic
# Define las rutas de la API y las páginas web

from django.urls import path, include
from rest_framework import routers
from . import views

# ============================================
# CONFIGURACIÓN DEL ROUTER DE DRF
# ============================================

# DefaultRouter: Crea automáticamente las rutas para las vistas de la API
router = routers.DefaultRouter()

# Registrar cada ViewSet con su endpoint
# router.register(r'endpoint', ViewSet)
router.register(r'teachers', views.TeacherViewSet)      # /api/teachers/
router.register(r'students', views.StudentViewSet)      # /api/students/
router.register(r'courses', views.CourseViewSet)        # /api/courses/
router.register(r'enrollments', views.StudentCourseViewSet)  # /api/enrollments/

# ============================================
# LISTA DE PATRONES DE URL
# ============================================

urlpatterns = [
    # --- Rutas de la API (DRF) ---
    # Todas las rutas del router están bajo el prefijo 'api/'
    path('api/', include(router.urls)),
    
    # --- Rutas de las páginas web ---
    # Página de inicio (home)
    path('', views.home_view, name='home'),
    # Página de cursos
    path('courses/', views.courses_view, name='courses'),
    # Página de estudiantes
    path('students/', views.students_view, name='students'),
]