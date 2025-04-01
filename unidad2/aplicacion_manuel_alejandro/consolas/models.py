from django.db import models

# Create your models here.

class Consolas(models.Model):
    potencia_de_procesamiento = models.CharField(max_length=100)
    capacidad_de_almacenamiento = models.CharField(max_length=100)
    conectividad = models.CharField(max_length=100)
    diseño_y_ergonomía = models.CharField(max_length=100)

    def __str__(self):
        return self.potencia_de_procesamiento