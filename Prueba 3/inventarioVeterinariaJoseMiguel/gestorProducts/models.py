from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
