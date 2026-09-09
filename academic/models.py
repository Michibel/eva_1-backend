# academic/models.py
# Modelos de datos para el Sistema de Gestión Académica
# Basados en el modelo ER proporcionado en la evaluación

from django.db import models

# Create your models here.

class Teacher(models.Model):
    """
    Modelo que representa a un Profesor/Docente
    Atributos:
        - first_name: Nombre del profesor (máximo 50 caracteres)
        - last_name: Apellido del profesor (máximo 50 caracteres)
    """
    first_name = models.CharField(max_length=50)  # Campo de texto para el nombre
    last_name = models.CharField(max_length=50)   # Campo de texto para el apellido

    def __str__(self):
        """Método que devuelve la representación en string del objeto"""
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    """
    Modelo que representa a un Estudiante
    Atributos:
        - first_name: Nombre del estudiante (máximo 50 caracteres)
        - last_name: Apellido del estudiante (máximo 50 caracteres)
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    """
    Modelo que representa un Curso/Asignatura
    Atributos:
        - name: Nombre del curso (máximo 100 caracteres)
        - teacher: Relación Many-to-One con Teacher (ForeignKey)
    """
    name = models.CharField(max_length=100)  # Nombre del curso
    # ForeignKey: Un profesor puede tener muchos cursos
    # on_delete=models.CASCADE: Si se elimina un profesor, se eliminan sus cursos
    # related_name='courses': Permite acceder a los cursos desde teacher.courses
    teacher = models.ForeignKey(
        Teacher, 
        on_delete=models.CASCADE, 
        related_name='courses'
    )

    def __str__(self):
        return self.name


class StudentCourse(models.Model):
    """
    Modelo intermedio (Tabla de inscripción) para la relación Many-to-Many
    entre Student y Course
    Atributos:
        - student: Relación Many-to-One con Student
        - course: Relación Many-to-One con Course
    """
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='courses'
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='students'
    )

    class Meta:
        # unique_together: Evita que un estudiante se inscriba dos veces al mismo curso
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}"