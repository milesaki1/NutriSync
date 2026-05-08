from django.db import models


# Opciones predefinidas para asegurar integridad de datos (usado en modelos y formularios)
class TipoComida(models.TextChoices):
    DESAYUNO = "DE", "Desayuno"
    ALMUERZO = "AL", "Almuerzo"
    CENA = "CE", "Cena"
    SNACK = "SN", "Snack"


class Sexo(models.TextChoices):
    MASCULINO = "M", "Masculino"
    FEMENINO = "F", "Femenino"


class NivelActividad(models.TextChoices):
    SEDENTARIO = "SE", "Sedentario"
    LIGERO = "LI", "Ligero"
    MODERADO = "MO", "Moderado"
    INTENSO = "IN", "Intenso"
    MUY_INTENSO = "MI", "Muy intenso"


class Objetivo(models.TextChoices):
    PERDER_PESO = "PP", "Perder peso"
    MANTENER = "MA", "Mantener peso"
    GANAR_MASA = "GM", "Ganar masa muscular"


class TipoEjercicio(models.TextChoices):
    CARDIO = "CA", "Cardio"
    FUERZA = "FU", "Fuerza"
    YOGA = "YO", "Yoga"
    CAMINATA = "CM", "Caminata"
    OTRO = "OT", "Otro"


class EstadoGeneral(models.IntegerChoices):
    ACTIVO = 1, "Activo"
    DE_BAJA = 9, "De baja"
