from rest_framework import viewsets
from api.models import Autor
from api.serializers import AutorSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
