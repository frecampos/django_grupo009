from django.db import models

# Create your models here.

# Crear las tablas para SliderGaleria y MisionyVision
class SliderIndex(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident

# Crear tabla de Insumos.

class Insumos(models.Model):
    nombre = models.CharField(max_length=120, primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class MisionyVision(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()


    def __str__(self):
        return self.ident
