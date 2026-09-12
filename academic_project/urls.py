# academic_project/urls.py
# Configuración principal de URLs con redirección

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academic.urls')),
    
    # Redirección al inicio para URLs no encontradas
    path('<path:unknown>', RedirectView.as_view(url='/', permanent=False)),
]