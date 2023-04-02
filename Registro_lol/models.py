from django.db import models

# Create your models here.

class Crear_campeon(models.Model):
    nombre_campeon = models.CharField(max_length=10)
    dificultad_campeon = models.IntegerField(1)
    descripcion_campeon = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.nombre_campeon} - {self.dificultad_campeon} - {self.descripcion_campeon}"
    
class Crear_ward(models.Model):
    nombre_ward = models.CharField(max_length=10)
    rango_vision = models.IntegerField(2)
    descripcion_ward = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.nombre_ward} - {self.rango_vision} - {self.descripcion_ward}"
    
class Crear_mapa(models.Model):
    nombre_mapa = models.CharField(max_length=10)
    cantidad_jugadores = models.IntegerField(2)
    descripcion_mapa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.nombre_mapa} - {self.cantidad_jugadores} - {self.descripcion_mapa}"