from django.db import models
from clientes.models import tabla_cliente
# Create your models here.
class tabla_citas(models.Model):
    paciente = models.OneToOneField(tabla_cliente, on_delete=models.CASCADE)
    fechayhora = models.DateField()