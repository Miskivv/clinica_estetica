# clinicapp/urls.py - CORREGIDO

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'), # Acceso de Pacientes
    path('register/', views.register_view, name='register'), # ¡Corregido aquí!
    path('reservar/', views.reserve_appointment, name='reserve_appointment'), # Agendar Cita
    path('mis-citas/', views.my_appointments, name='my_appointments'), # Mis Citas Agendadas
    path('logout/', views.logout_view, name='logout'),
    path('servicios/', views.services_view, name='services'),
    path('panel/recepcion/', views.panel_recepcion_view, name='panel_recepcion'),
]
