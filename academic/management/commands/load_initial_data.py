# academic/management/commands/load_initial_data.py
# Script personalizado para cargar datos iniciales desde un archivo JSON
# Se ejecuta con: python manage.py load_initial_data

import json
import os
from django.core.management.base import BaseCommand
from academic.models import Teacher, Student, Course, StudentCourse


class Command(BaseCommand):
    """
    Comando personalizado de Django para cargar datos iniciales
    """
    help = 'Carga datos iniciales desde un archivo JSON en fixtures/'

    def handle(self, *args, **options):
        """
        Método principal que se ejecuta al llamar al comando
        """
        # ============================================
        # PASO 1: Buscar el archivo JSON
        # ============================================
        # Ruta donde se encuentra el archivo de datos
        json_file_path = os.path.join(
            os.path.dirname(__file__), 
            '../../fixtures/initial_data.json'
        )
        
        # Verificar si el archivo existe en la ruta esperada
        if not os.path.exists(json_file_path):
            # Intentar con ruta alternativa
            json_file_path = os.path.join(
                os.path.dirname(__file__),
                '../initial_data.json'
            )

        try:
            # Intentar abrir y leer el archivo JSON
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            # Si no se encuentra el archivo, mostrar error
            self.stdout.write(self.style.ERROR('❌ No se encontró el archivo initial_data.json'))
            self.stdout.write('Asegúrate de que el archivo está en academic/fixtures/')
            return

        # ============================================
        # PASO 2: Limpiar datos existentes
        # ============================================
        # Se eliminan todos los datos para evitar duplicados
        self.stdout.write('🧹 Eliminando datos existentes...')
        StudentCourse.objects.all().delete()
        Course.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()

        # ============================================
        # PASO 3: Cargar nuevos datos
        # ============================================
        self.stdout.write('📥 Cargando nuevos datos...')
        
        for item in data:
            # Extraer información del elemento
            model_name = item.get('model')
            fields = item.get('fields')
            pk = item.get('pk')  # Primary Key

            # Crear el objeto según el modelo
            if model_name == 'academic.teacher':
                Teacher.objects.create(id=pk, **fields)
                self.stdout.write(f'  ✓ Profesor {fields["first_name"]} {fields["last_name"]} creado.')

            elif model_name == 'academic.student':
                Student.objects.create(id=pk, **fields)
                self.stdout.write(f'  ✓ Estudiante {fields["first_name"]} {fields["last_name"]} creado.')

            elif model_name == 'academic.course':
                Course.objects.create(id=pk, **fields)
                self.stdout.write(f'  ✓ Curso {fields["name"]} creado.')

            elif model_name == 'academic.studentcourse':
                StudentCourse.objects.create(id=pk, **fields)
                self.stdout.write(f'  ✓ Inscripción estudiante {fields["student"]} en curso {fields["course"]} creada.')

        # ============================================
        # PASO 4: Confirmación de éxito
        # ============================================
        self.stdout.write(self.style.SUCCESS('✅ Datos iniciales cargados exitosamente!'))