from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    fecha_de_publicacion = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Libro
        fields = '__all__'