# clinicapp/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Service, Specialist, Appointment # Asume que estos modelos existirán

# 1. Formulario de Registro de Usuario (Se usa en register_view)
class RegisterForm(UserCreationForm):
    # Por defecto, UserCreationForm solo pide username y password.
    # Si quieres añadir email, necesitas modificar o usar un formulario diferente
    # o añadir el campo aquí. Para simplificar, usamos el base por ahora.
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


# 2. Formulario de Reserva de Citas (Se usa en reserve_appointment)
# Este formulario usa los Modelos de la Base de Datos.
# Asume que los campos se llaman 'service', 'specialist' y 'date'.
class AppointmentForm(forms.ModelForm):
    # Aquí puedes personalizar los widgets para que se vean como en el video
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd-mm-aaaa'}),
        input_formats=['%Y-%m-%d', '%d-%m-%Y'], # Asegura que maneje el formato
        label="Fecha de la Cita"
    )

    class Meta:
        model = Appointment
        fields = ['service', 'specialist', 'date']
        # Los campos 'service' y 'specialist' se rellenarán automáticamente
        # con un queryset de los modelos Service y Specialist.
        labels = {
            'service': 'Servicio',
            'specialist': 'Especialista',
        }