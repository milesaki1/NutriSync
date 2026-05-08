from django.db import models
from django.utils import timezone


class RegistroQuerySet(models.QuerySet):
    """Encapsula la lógica de consultas para los registros de comida y hábitos"""

    def de_hoy(self):
        """Filtra registros realizados el día de hoy"""
        return self.filter(fecha=timezone.now().date())

    def ultima_semana(self):
        """Filtra registros de los últimos 7 días"""
        hace_una_semana = timezone.now().date() - timezone.timedelta(days=7)
        return self.filter(fecha__gte=hace_una_semana)

    def con_items(self):
        """Optimiza la consulta cargando los items y sus alimentos relacionados"""
        return self.prefetch_related("items__alimento")
