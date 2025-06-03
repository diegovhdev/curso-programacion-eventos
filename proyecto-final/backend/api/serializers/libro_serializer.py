from rest_framework import serializers
from api.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    fecha_de_publicacion = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Libro
        fields = '__all__'