import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from academic.models import Teacher, Student, Course, StudentCourse

class Command(BaseCommand):
    help = 'Carga datos iniciales desde un archivo JSON'

    def handle(self, *args, **options):
        # Ruta al archivo JSON
        json_file_path = os.path.join(os.path.dirname(__file__), 'initial_data.json')

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for item in data:
            model_name = item.get('model')
            fields = item.get('fields')

            if model_name == 'academic.teacher':
                Teacher.objects.create(**fields)
                self.stdout.write(f"  - Profesor {fields['first_name']} {fields['last_name']} creado.")

            elif model_name == 'academic.student':
                Student.objects.create(**fields)
                self.stdout.write(f"  - Estudiante {fields['first_name']} {fields['last_name']} creado.")

            elif model_name == 'academic.course':
                Course.objects.create(**fields)
                self.stdout.write(f"  - Curso {fields['name']} creado.")

            elif model_name == 'academic.studentcourse':
                StudentCourse.objects.create(**fields)
                self.stdout.write(f"  - Inscripción de estudiante {fields['student']} en curso {fields['course']} creada.")

        self.stdout.write(self.style.SUCCESS('Datos iniciales cargados exitosamente.'))