from django.db import models

# Create your models here.
class tabla_cliente(models.Model):
    nombre = models.CharField(max_length=35)
    edad = models.PositiveSmallIntegerField()
    peso = models.FloatField()
    altura = models.FloatField()

    def __str__(self):
        return self.nombre
    