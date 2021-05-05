from django.forms import ModelForm
from django import forms
from .models import tabla_citas

class AgregarCitas(ModelForm):
    class Meta:
        model = tabla_citas
        fields = '__all__'