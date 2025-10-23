# models.py
# Define el modelo de datos para el inventario escolar

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del equipo
    categoria = models.CharField(max_length=50)  # Tipo de equipo (Notebook, Proyector, etc.)
    estado = models.CharField(max_length=50)  # Estado actual del equipo
    fecha_ingreso = models.DateField()  # Fecha en que fue agregado al inventario
    ubicacion = models.CharField(max_length=100)  # Lugar donde se encuentra el equipo

    def __str__(self):
        return self.nombre
