from django.db import models


# QuerySet personalizado para encapsular la lógica de consultas de la tabla Alimento
class AlimentoQuerySet(models.QuerySet):
    # Filtra y devuelve únicamente los alimentos que están activos
    def activos(self):
        from config.choices import EstadoGeneral

        return self.filter(estado=EstadoGeneral.ACTIVO)

    # Realiza una búsqueda de alimentos activos que contengan el texto de búsqueda (sin importar mayúsculas/minúsculas)
    def buscar(self, q):
        return self.activos().filter(nombre__icontains=q)

    # Filtra y devuelve los alimentos activos que corresponden a la gastronomía peruana
    def peruanos(self):
        return self.activos().filter(es_peruano=True)
