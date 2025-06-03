from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    