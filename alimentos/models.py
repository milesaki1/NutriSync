from django.db import models
from config.choices import EstadoGeneral
from .querysets import AlimentoQuerySet


# Modelo que representa un alimento en el sistema
class Alimento(models.Model):
    # Manager personalizado para filtros rápidos (ej. objetos peruanos o activos)
    objects = AlimentoQuerySet.as_manager()

    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100, blank=True, default="")
    calorias_100g = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    proteinas_100g = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    carbohidratos_100g = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    grasas_100g = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fibra_100g = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    es_peruano = models.BooleanField(default=False)
    estado = models.IntegerField(
        choices=EstadoGeneral.choices, default=EstadoGeneral.ACTIVO
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "alimentos"
        ordering = ["nombre"]

    def __str__(self):
        if self.marca:
            return f"{self.nombre} ({self.marca})"
        return self.nombre
