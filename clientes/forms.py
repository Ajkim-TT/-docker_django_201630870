from django.forms import ModelForm
from django import forms
from .models import tabla_cliente

class AgregarCliente(ModelForm):
    class Meta:
        model = tabla_cliente
        fields = '__all__'