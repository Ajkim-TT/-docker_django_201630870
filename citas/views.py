from django.shortcuts import render
from .models import tabla_citas
from clientes.models import tabla_cliente
from .forms import AgregarCitas
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def ver_citas(request):
    datos = tabla_citas.objects.all()
    context = {'entradas':datos}
    if request.method == 'POST':
        if request.POST.get('fecha')==None:
            tabla_citas.objects.all().delete()
            datos = tabla_citas.objects.all()
            context = {'entradas':datos}
        else:
            date = request.POST.get('fecha')
            datos = tabla_citas.objects.filter(fechayhora=date)
            context = {'entradas':datos}
    return render(request,"view_appointment.html",context)
@login_required(login_url='login')
def agregar_citas(request):
    formulario = AgregarCitas()
    if request.method == 'POST':
        dato = tabla_citas()
        formulario = AgregarCitas(request.POST)
        if formulario.is_valid():
            formulario.save()
            context = {'forms':formulario}
            return render(request,"add_appointment.html",context)
    context = {'forms':formulario}
    return render(request,"add_appointment.html",context)
