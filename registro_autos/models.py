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
        return f'{self.id} - {self.fecha} - {self.nombre} - {self.apellido} - {self.email} - {self.telefono} - {self.vehiculo} - {self.comentario}'

class PreciosServicios(models.Model):

    precio_mecanica = models.IntegerField()
    precio_mantenimiento = models.IntegerField()
    precio_lavado = models.IntegerField()
    precio_pintura = models.IntegerField()
