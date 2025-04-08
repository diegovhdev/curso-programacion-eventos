from django.shortcuts import render
from rest_framework import viewsets
from .models import Videojuegos
from .serializers import VideojuegoSerializer

class VideojuegosViewSet(viewsets.ModelViewSet):
    queryset = Videojuegos.objects.all()
    serializer_class = VideojuegoSerializer
