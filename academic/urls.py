# academic/urls.py
# Configuración de URLs con Dashboard

from django.urls import path, include
from rest_framework import routers
from . import views

# ============================================
# CONFIGURACIÓN DEL ROUTER DE DRF
# ============================================

router = routers.DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'enrollments', views.StudentCourseViewSet)

# ============================================
# LISTA DE PATRONES DE URL
# ============================================

urlpatterns = [
    # Rutas de la API (DRF)
    path('api/', include(router.urls)),
    
    # Rutas de las páginas web
    path('', views.dashboard_view, name='dashboard'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('courses/', views.courses_view, name='courses'),
    path('students/', views.students_view, name='students'),
]