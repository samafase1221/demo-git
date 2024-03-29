from django.db import models

# Create your models here.
class PersonaSoporte(models.Model):
    nombre = models.CharField(max_length=64)
    edad = models.IntegerField(null=True, blank=True)	
    activo = models.BooleanField(default=True)

class PQR(models.Model):
    persona_soporte = models.ForeignKey(PersonaSoporte, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=32)
    comentario = models.TextField(blank=True)
    creacion = models.DateField()
    