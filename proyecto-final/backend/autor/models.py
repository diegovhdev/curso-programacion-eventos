from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

