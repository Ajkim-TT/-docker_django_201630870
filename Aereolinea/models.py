from django.db import models

# Create your models here.
class VueloFactura(models.Model):
    clase = models.CharField(max_length=10)
    comida = models.SmallIntegerField()
    bebida = models.SmallIntegerField()
    pelicula = models.SmallIntegerField()
    servicios = models.SmallIntegerField()
    subtotal = models.FloatField()
    descuentoM = models.FloatField()
    total = models.FloatField()
