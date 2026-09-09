from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'teachers', views.TeacherViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'enrollments', views.StudentCourseViewSet)

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),

    # Rutas de las páginas web
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('students/', views.students_view, name='students'),
]