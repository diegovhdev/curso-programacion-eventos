from django.db import models

# Create your models here.

class Videojuegos(models.Model):

    opciones_graficos = [
        ('2D', '2D'),
        ('3D', '3D')
    ]

    titulo = models.CharField(max_length=100)
    graficos = models.CharField(max_length=3, choices=opciones_graficos, default='2D')
    motor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_de_creacion = models.DateField()

    def __str__(self):
        return self.titulo
