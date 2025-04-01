from django.shortcuts import render
from rest_framework import viewsets
from .models import Consolas
from .serializers import ConsolaSerializers

class ConsolasViewSet(viewsets.ModelViewSet):
    queryset = Consolas.objects.all()
    serializer_class = ConsolaSerializers