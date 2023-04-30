from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

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

def reserva(self): # Revisar la multiplicidad de guardados
    
    if self.method == 'POST':
      
        miTurno = Formturno(self.POST)
        if miTurno.is_valid():        
            data = miTurno.cleaned_data
            turno = Turno(fecha=data['fecha'], nombre=data['nombre'], apellido=data['apellido'], email=data['email'], telefono=data['telefono'], vehiculo=data['vehiculo'], comentario=data['comentario'])
            turno.save()   
            return render(self, "confirmaTurno.html", {"nro_turno": turno.id})   
        else:          
            return render(self, "inicio.html", {"mensaje": "Formulario invalido"})    
    else:
        miTurno = Formturno()
        return render(self, "reservaturno.html", {"miTurno": miTurno})
    
def register(request):
    
    print('method: ', request.method)
    print('post: ', request.POST)
  
    if request.method == 'POST':
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, 'confirmaRegistro.html')
            
        else:
            return render(request, "loginRegistro.html")
    else:
        miFormulario = UserCreationForm()
        return render(request, "loginRegistro.html", {"miFormulario": miFormulario})   

def conf_registro(self):

    return render(self,"confirmaRegistro.html")

def loginView(request):
   
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user)
                return render(request, 'confirmaLogin.html')
            
            else:
                return render(request, 'inicio.html', {"mensaje": f'Error: datos incorrectos'})
            
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        miFormulario = AuthenticationForm()
        return render(request, "loginRegistro.html", {"miFormulario": miFormulario})
  
def conf_ingreso(self):

    return render(self,"confirmaLogin.html")

@login_required
def VistaTurno(request):
    email = request.user.email
    turnos = Turno.objects.filter(email=email)
    return render(request, 'user.html', {'turnos': turnos})

class DetalleTurno(DetailView):

    model = Turno
    template_name = 'userTurnoDetail.html'
    context_object_name = 'turno'