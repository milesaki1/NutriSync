from django.contrib import admin
from .models import Alimento


# Registra el modelo Alimento en el panel de administrador para gestionarlo visualmente
@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "marca",
        "calorias_100g",
        "proteinas_100g",
        "es_peruano",
        "estado",
    )
    search_fields = ("nombre", "marca")
    list_filter = ("es_peruano", "estado")
