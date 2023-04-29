from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [   
    path('', inicio, name="inicio"),
    path('SeleccionaTurno/', seleccion_turno, name="reservaturno"),
    path('MuestraServicios/', servicios, name="muestraservicios"),
    path('MuestraProductos/', productos, name="muestraproductos"),
    path('MuestraNovedades/', novedades, name="muestranovedades"),
    path('Nostros/', nosotros, name="nosotros"),
    path('MuestraContacto/', contacto, name="muestracontacto"),
    path('ConfirmaTurno/', reserva, name="confirmaturno"),


]