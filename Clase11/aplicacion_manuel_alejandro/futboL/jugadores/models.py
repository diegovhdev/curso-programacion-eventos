from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero_dorsal = models.PositiveIntegerField()
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.numero_dorsal})"