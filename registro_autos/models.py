from django.db import models

class Turno(models.Model):

    fecha = models.DateField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    vehiculo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.fecha} - {self.telefono} - {self.vehiculo} - {self.comentario}'

""" class Usuarios(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50) """