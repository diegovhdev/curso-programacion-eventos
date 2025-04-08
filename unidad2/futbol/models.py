from django.db import models

class futbol (models.Model):
    nombre= models.CharField(max_length=100)
    posicion= models.CharField(max_length=1)
    edad= models.IntegerField()
    
    def __srt__(self):
        return self.nombre
    
# Create your models here.
