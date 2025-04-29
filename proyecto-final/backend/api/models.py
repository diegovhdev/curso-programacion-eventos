from django.db import models
from rest_framework.fields import DateField

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    paginas = models.IntegerField()
    fecha_de_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

