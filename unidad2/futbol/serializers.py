from rest_framework import serializers
from .models import futbol

class futbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = futbol
        fields= '__all__'