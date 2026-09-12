# academic_project/urls.py
# Configuración principal de URLs del proyecto
# Incluye redirección al inicio para URLs no encontradas

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Panel administrativo de Django
    path('admin/', admin.site.urls),
    
    # Todas las rutas de la aplicación academic
    path('', include('academic.urls')),
    
    # ============================================
    # REDIRECCIÓN AL INICIO PARA URLs NO ENCONTRADAS
    # ============================================
    # Cualquier URL que no coincida con las anteriores
    # será redirigida a la página de inicio
    path('<path:unknown>', RedirectView.as_view(url='/', permanent=False)),
]