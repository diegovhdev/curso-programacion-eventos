from django.shortcuts import render
from rest_framework import viewsets
from .models import futbol
from .serializers import futbolSerializer

class futbolViewset(viewsets.ModelViewSet):
    queryset = futbol.objects.all()
    serializer_class= futbolSerializer
# Create your views here.
