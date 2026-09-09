# academic_project/urls.py
# Configuración principal de URLs del proyecto

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel administrativo de Django
    path('admin/', admin.site.urls),
    
    # Todas las rutas de la aplicación academic
    # (incluye API y páginas web)
    path('', include('academic.urls')),
]