from django.shortcuts import render
from rest_framework import viewsets
from .models import Clientes
from .serializers import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer
