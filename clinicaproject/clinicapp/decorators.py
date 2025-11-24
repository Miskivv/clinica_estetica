# clinicapp/decorators.py

from django.shortcuts import redirect
from functools import wraps
# ¡BORRA LA LÍNEA 'from .models import Role' o verifica que no exista!

def recepcionista_required(view_func):
    """
    Decorador que verifica si el usuario es un 'Recepcionista' usando Grupos de Django.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verifica si el usuario está autenticado Y pertenece al grupo 'Recepcionista'
        if request.user.is_authenticated and request.user.groups.filter(name='Recepcionista').exists():
            return view_func(request, *args, **kwargs)
        
        # Si no cumple el requisito, lo redirige a la página de login
        return redirect('login') 
    return wrapper