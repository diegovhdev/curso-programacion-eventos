from django.shortcuts import render
from rest_framework import viewsets
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

