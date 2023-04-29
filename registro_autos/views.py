from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.http import QueryDict
from urllib.parse import urlencode

def inicio(self):

    return render(self, "inicio.html")

def seleccion_turno(self):

    return render(self,"reservaturno.html")

def servicios(self):

    return render(self,"servicios.html")

def productos(self):

    return render(self,"productos.html")

def nosotros(self):

    return render(self,"nosotros.html")

def novedades(self):

    return render(self,"novedades.html")

def contacto(self):

    return render(self,"contacto.html")

def reserva(request):
    
    print('POST data: ', dict(request.POST))

    if request.method == 'POST':
      
      miTurno = Formturno(request.POST)
      if miTurno.is_valid():        
          data = miTurno.cleaned_data
          turno = Turno(fecha=data['fecha'], nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], vehiculo=data['vehiculo'], comentario=data['comentario'])
          turno.save()   
          return render(request, "confirmaciónTurno.html")   
      else:          
          return render(request, "inicio.html", {"mensaje": "Formulario invalido"})    
    else:
      miTurno = Formturno()
      return render(request, "reservaturno.html", {"miTurno": miTurno})

