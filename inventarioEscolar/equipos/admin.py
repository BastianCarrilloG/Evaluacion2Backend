
# Configuración del panel de administración para el modelo Equipo

from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista
    list_display = ("nombre", "categoria", "estado", "fecha_ingreso", "ubicacion")
    
    # Filtros laterales para facilitar búsqueda por estado o categoría
    list_filter = ("categoria", "estado", "ubicacion")

    # Ordenar los registros (del más reciente al más antiguo)
    ordering = ("-fecha_ingreso", "nombre")
