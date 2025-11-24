# clinicapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # El error en tu video sugiere que algo pasa aquí o en la redirección.
            # Asumiendo que el formulario funciona, se guarda el usuario y se hace login:
            login(request, user)
            return redirect('home') # Redirige a la página de inicio o a la de agendar citas
    else:
        form = RegisterForm()
    
    # Renderiza la plantilla 'register.html'
    return render(request, 'clinicapp/register.html', {'form': form})
# clinicapp/views.py

from django.contrib.auth.decorators import login_required
# Asumo que tienes un modelo Appointment y un formulario AppointmentForm

@login_required
def reserve_appointment(request):
    # Lógica para manejar la reserva de citas (POST) y mostrar el formulario (GET)
    if request.method == 'POST':
        # ... procesar formulario de reserva
        pass
    
    # Muestra la plantilla 'reserve_appointment.html'
    return render(request, 'reserve_appointment.html') 

@login_required
def my_appointments(request):
    # Lógica para obtener y mostrar las citas del usuario actual
    # appointments = Appointment.objects.filter(patient=request.user)
    
    # Muestra la plantilla 'my_appointments.html'
    return render(request, 'my_appointments.html', {'appointments': []})

# clinicapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, AppointmentForm
# Necesitas crear un archivo models.py si aún no lo tienes para que esto funcione
from .models import Service, Specialist, Appointment 


# --- Vistas Básicas y Autenticación ---

# 1. Inicio (path='')
def home(request):
    """Muestra la página de inicio (0:00 - 0:09 en el video)."""
    return render(request, 'clinicapp/home.html', {
        'services': Service.objects.all()[:3], # Muestra algunos servicios en la home
        'specialists': Specialist.objects.all()[:3] # Muestra algunos especialistas
    })

# 2. Vistas de Servicios (path='servicios/') - Visto en 0:02
def services_view(request):
    """Muestra todos los tratamientos/servicios."""
    services = Service.objects.all()
    # Si no hay servicios, muestra el mensaje "Aún no hay servicios disponibles."
    return render(request, 'clinicapp/services.html', {'services': services})

# 3. Acceso de Pacientes / Login (path='login/') - Visto en 0:10
def login_view(request):
    """Maneja el inicio de sesión."""
    # Aquí usarías la forma estándar de Django para el login (AuthenticationForm)
    if request.method == 'POST':
        # ... lógica de autenticación ...
        pass
    return render(request, 'clinicapp/login.html')

# 4. Crear Cuenta / Registro (path='register/') - Visto en 0:48
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Esto es lo que verifica las credenciales y las guarda en la sesión
            login(request, form.get_user()) 
            # Redirige a donde el usuario iba (si usó /reservar/?next=...) o a 'home'
            return redirect('home') 
        # Si no es válido, vuelve a renderizar el formulario con errores
    else:
        form = AuthenticationForm()
        
    return render(request, 'clinicapp/login.html', {'form': form})

# 5. Cerrar Sesión (path='logout/')
def logout_view(request):
    """Cierra la sesión del usuario."""
    logout(request)
    return redirect('home')


# --- Vistas Protegidas (Requieren Login) ---

# 6. Agendar Nueva Cita (path='reservar/') - Visto en 0:22
@login_required # Asegura que solo usuarios logueados puedan acceder
def reserve_appointment(request):
    """Maneja la reserva de citas."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.patient = request.user # Asigna el paciente logueado
            reservation.save()
            messages.success(request, "Cita reservada con éxito.")
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    
    # Muestra la plantilla 'reserve_appointment.html'
    return render(request, 'clinicapp/reserve_appointment.html', {'form': form})

# 7. Mis Citas Agendadas (path='mis-citas/') - Visto en 0:34
@login_required
def my_appointments(request):
    """Muestra todas las citas agendadas por el usuario actual."""
    # Obtiene solo las citas del usuario logueado
    appointments = Appointment.objects.filter(patient=request.user).order_by('date')
    
    # Muestra la plantilla 'my_appointments.html'
    return render(request, 'clinicapp/my_appointments.html', {'appointments': []})
from .decorators import recepcionista_required
@login_required # Opcional: asegura que esté logueado
@recepcionista_required # <-- ¡Aplica la restricción de grupo!
def panel_recepcion_view(request):
    """Muestra el panel de control para el personal de Recepción."""
    
    # Lógica para mostrar las citas del día, etc.
    
    # Asegúrate de que la ruta de la plantilla esté correcta: 'clinicapp/panel_recepcion.html'
    return render(request, 'clinicapp/panel_recepcion.html', {
        # 'citas_del_dia': citas
    })