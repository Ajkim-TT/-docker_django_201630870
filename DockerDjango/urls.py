"""DockerDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import main_pag
from Login import views as vLog
from Aereolinea import views as vAereo
from clientes import views as vCli
from citas import views as vCit

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('principal/',main_pag,name='principal'),
    path('login/',vLog.login_pag, name='login'),
    path('logout/',vLog.logout_page, name='logout'),
    path('register/',vLog.register_pag, name='register'),
    path('orden/',vAereo.Ordenar,name = 'Orden'),
    path('factura/',vAereo.Factura,name = 'Factura'),
    path('historial/',vAereo.historial,name = 'Historial'),
    path('agregar_cliente/',vCli.agregar_cliente, name = 'add_cliente'),
    path('ver_cliente/',vCli.ver_clientes,name = 'view_cliente'),
    path('ver_cita/',vCit.ver_citas, name = 'view_appointment'),
    path('agregar_cita/',vCit.agregar_citas, name = 'add_appointment'),
]
