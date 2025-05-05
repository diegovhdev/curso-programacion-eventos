from rest_framework import serializers
from .models import Consolas

class ConsolaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consolas
        fields = '__all__'
