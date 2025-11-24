# clinicapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 1. Modelo de Servicio/Tratamiento
class Service(models.Model):
    """Representa un tipo de tratamiento que ofrece la clínica."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Servicio")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Precio Estimado")

    def __str__(self):
        return self.name

# 2. Modelo de Especialista
class Specialist(models.Model):
    """Representa a un médico o especialista que realiza tratamientos."""
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    specialty = models.CharField(max_length=100, verbose_name="Especialidad Principal")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# 3. Modelo de Cita
class Appointment(models.Model):
    """Representa una cita agendada por un paciente."""
    # Enlace al usuario que agendó la cita (Paciente)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Paciente")
    
    # Enlace al servicio seleccionado
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Servicio")
    
    # Enlace al especialista asignado
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, verbose_name="Especialista")
    
    # Fecha y hora de la cita
    date = models.DateField(verbose_name="Fecha de la Cita")
    time = models.TimeField(default=timezone.now, verbose_name="Hora de la Cita")

    # Estado de la cita (ej. Pendiente, Confirmada, Cancelada)
    STATUS_CHOICES = [
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('X', 'Cancelada'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
        verbose_name="Estado"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        # Asegura que un especialista no tenga dos citas al mismo tiempo exacto
        unique_together = ('specialist', 'date', 'time') 

    def __str__(self):
        return f"Cita de {self.patient.username} con {self.specialist} para {self.service.name} el {self.date}"# clinicapp/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 1. Modelo de Servicio/Tratamiento
class Service(models.Model):
    """Representa un tipo de tratamiento que ofrece la clínica."""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Servicio")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name="Precio Estimado")

    def __str__(self):
        return self.name

# 2. Modelo de Especialista
class Specialist(models.Model):
    """Representa a un médico o especialista que realiza tratamientos."""
    first_name = models.CharField(max_length=50, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Apellido")
    specialty = models.CharField(max_length=100, verbose_name="Especialidad Principal")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# 3. Modelo de Cita
class Appointment(models.Model):
    """Representa una cita agendada por un paciente."""
    # Enlace al usuario que agendó la cita (Paciente)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Paciente")
    
    # Enlace al servicio seleccionado
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Servicio")
    
    # Enlace al especialista asignado
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, verbose_name="Especialista")
    
    # Fecha y hora de la cita
    date = models.DateField(verbose_name="Fecha de la Cita")
    time = models.TimeField(default=timezone.now, verbose_name="Hora de la Cita")

    # Estado de la cita (ej. Pendiente, Confirmada, Cancelada)
    STATUS_CHOICES = [
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('X', 'Cancelada'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
        verbose_name="Estado"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        # Asegura que un especialista no tenga dos citas al mismo tiempo exacto
        unique_together = ('specialist', 'date', 'time') 

    def __str__(self):
        return f"Cita de {self.patient.username} con {self.specialist} para {self.service.name} el {self.date}"