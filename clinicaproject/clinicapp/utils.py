from datetime import date

def calcular_descuento_cumpleaños(paciente_perfil):
    """
    Verifica si hoy es el cumpleaños del paciente y aplica un 20% de descuento.
    :param paciente_perfil: Instancia del modelo Paciente (que contiene fecha_nacimiento).
    :return: Tasa de descuento (0.20 o 0.0).
    """
    if paciente_perfil and paciente_perfil.fecha_nacimiento:
        hoy = date.today()
        if (paciente_perfil.fecha_nacimiento.day == hoy.day and 
            paciente_perfil.fecha_nacimiento.month == hoy.month):
            return 0.20 
    return 0.0