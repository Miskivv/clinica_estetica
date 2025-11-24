# clinicapp/admin.py

from django.contrib import admin
from .models import Service, Specialist, Appointment

# --- Configuración para el Modelo Service ---
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Service en el panel de administración.
    """
    # Columnas a mostrar en la lista (display)
    list_display = ('name', 'price', 'id')
    
    # Campos que permiten la búsqueda
    search_fields = ('name', 'description')
    
    # Permite editar los campos directamente en la vista de lista
    list_editable = ('price',)

# --- Configuración para el Modelo Specialist ---
@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Specialist.
    """
    # Columnas a mostrar en la lista
    list_display = ('full_name', 'specialty', 'email')
    
    # Campos por los que se puede filtrar la lista
    list_filter = ('specialty',)
    
    # Campos que permiten la búsqueda
    search_fields = ('first_name', 'last_name', 'specialty')
    
    # Campos de solo lectura (no editables)
    readonly_fields = ('email',)
    
    # Cómo se muestran los campos al editar un especialista
    fieldsets = (
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Información Profesional', {
            'fields': ('specialty',)
        }),
    )

# --- Configuración para el Modelo Appointment ---
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Appointment (Citas).
    """
    # Columnas a mostrar en la lista
    list_display = ('patient', 'service', 'specialist', 'date', 'time', 'status', 'created_at')
    
    # Campos por los que se puede filtrar la lista
    list_filter = ('status', 'service', 'specialist', 'date')
    
    # Campos que permiten la búsqueda (permite buscar por el nombre de usuario del paciente)
    search_fields = ('patient__username', 'service__name', 'specialist__last_name')
    
    # Campos de solo lectura
    readonly_fields = ('created_at', 'patient')
    
    # Orden de las citas por defecto (las más nuevas o las más cercanas)
    ordering = ('date', 'time')