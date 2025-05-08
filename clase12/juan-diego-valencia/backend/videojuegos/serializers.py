from rest_framework import  serializers
from .models import Videojuegos

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuegos
        fields = '__all__'