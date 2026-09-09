# academic_project/settings.py
# Configuración principal del proyecto Django

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tu-clave-secreta-aqui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ============================================
# APLICACIONES INSTALADAS
# ============================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'academic',        # Nuestra aplicación academic
]

# ============================================
# MIDDLEWARE (Procesadores de peticiones)
# ============================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============================================
# CONFIGURACIÓN DE URLS
# ============================================

ROOT_URLCONF = 'academic_project.urls'

# ============================================
# CONFIGURACIÓN DE PLANTILLAS (HTML)
# ============================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Carpeta donde Django buscará plantillas
        'DIRS': [(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ============================================
# CONFIGURACIÓN WSGI
# ============================================

WSGI_APPLICATION = 'academic_project.wsgi.application'

# ============================================
# BASE DE DATOS (SQLite3 por defecto)
# ============================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================================
# VALIDACIÓN DE CONTRASEÑAS
# ============================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ============================================
# INTERNACIONALIZACIÓN
# ============================================

LANGUAGE_CODE = 'es-es'  # Idioma español
TIME_ZONE = 'America/Santiago'  # Zona horaria Chile
USE_I18N = True
USE_TZ = True

# ============================================
# ARCHIVOS ESTÁTICOS (CSS, JS, Imágenes)
# ============================================

STATIC_URL = 'static/'

# ============================================
# CAMPO POR DEFECTO PARA PRIMARY KEY
# ============================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'