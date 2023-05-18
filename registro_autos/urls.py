from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [   
    path('', inicio, name="inicio"),
    path('SeleccionaTurno/', seleccion_turno, name="reservaturno"),
    path('MuestraServicios/', servicios, name="muestraservicios"),
    path('MuestraProductos/', productos, name="muestraproductos"),
    path('MuestraNovedades/', novedades, name="muestranovedades"),
    path('Nostros/', nosotros, name="nosotros"),
    path('MuestraContacto/', contacto, name="muestracontacto"),
    path('ConfirmaTurno/', reserva, name="confirmaturno"),
    path('Login/', loginView, name="login"),
    path('registraUsuario/', register, name="registro"),
    path('ConfirmaRegistro/', conf_registro, name="confirmaregistro"),
    path('ConfirmaLogin/', conf_ingreso, name="confirmalogin"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('vistauser/', VistaUser, name="vistauser"),
    path('detalleturno/<pk>', DetalleTurno.as_view(), name="detalleturno"),
    path('datosEdicion/', editar_perfil, name="datosedicion"),
    path('eliminaTurno/<pk>', Eliminar_turno.as_view(), name="eliminaturno"),
    path('MuestraMecanica/', Mecanica, name="detalleMecanica"),
    path('MuestraMantenimiento/', Mantenimiento, name="detalleMantenimiento"),
    path('MuestraLavado/', Lavado, name="detalleLavado"),
    path('MuestraPintura/', Pintura, name="detallePintura"),
    
]