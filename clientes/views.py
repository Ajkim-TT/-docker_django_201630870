from django.shortcuts import render
from .models import tabla_cliente
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def agregar_cliente(request):
    if request.method == 'POST':
        dato = tabla_cliente()
        dato.nombre = request.POST['nombre']
        dato.edad = request.POST['edad']
        dato.peso = request.POST['peso']
        dato.altura = request.POST['altura']
        if not dato.nombre:
            messages.info(request,'AGREGE UN NOMBRE')
            return render(request,'add_client.html')
        if dato.nombre.isalpha() == False:
            messages.info(request,'NOMBRE CONTIENE CARACTERES INVALIDOS')
            return render(request,'add_client.html')
        if len(dato.nombre) > 35:
            messages.info(request,'NOMBRE ES DEMASIADO GRANDE')
            return render(request,'add_client.html')
        if float(dato.peso) < 0:
            messages.info(request,'EL PESO INGRESADO ES NEGATIVO')
            return render(request,'add_client.html')
        if float(dato.altura) < 0:
            messages.info(request,'LA ALTURA INGRESADA ES NEGATIVA')
            return render(request,'add_client.html')
        dato.save()
    context = {}
    return render(request,'add_client.html',context)
@login_required(login_url='login')
def ver_clientes(request):
    lista = tabla_cliente.objects.all()
    context = {
        'entradas':lista
    }
    if request.method == 'POST':
        tabla_cliente.objects.all().delete()
        lista = tabla_cliente.objects.all()
        context = {'entradas':lista}
        return render(request,'view_client.html',context)
    return render(request,'view_client.html',context)