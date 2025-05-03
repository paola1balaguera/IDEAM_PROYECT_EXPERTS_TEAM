from django.db import models
from django.contrib.auth.models import AbstractUser  

class ClasificacionExperto(models.TextChoices):
    PENDIENTE = 'pendiente'
    EN_PROGRESO = 'en progreso'
    COMPLETADA = 'completado'

class Experto(models.Model):
    experto_cc = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(null=False, max_length=255)
    segundo_nombre = models.CharField(null=False, max_length=255)
    primer_apellido = models.CharField(null=False, max_length=255)
    segundo_apellido = models.CharField(null=False, max_length=255)
    fecha_nacimiento = models.DateField(null=False, max_length=255)
    clasificacion = models.CharField(
        max_length=20,
        choices=ClasificacionExperto.choices
    )
    

    class Meta:
        managed = False
        db_table = 'experto'