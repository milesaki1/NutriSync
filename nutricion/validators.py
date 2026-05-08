from django.core.exceptions import ValidationError


def validar_cantidad_positiva(value):
    """Valida que la cantidad ingresada sea mayor a cero"""
    if value <= 0:
        raise ValidationError(
            f"La cantidad debe ser mayor a 0. Recibió: {value}"
        )
