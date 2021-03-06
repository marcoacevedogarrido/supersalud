from rest_framework import serializers, viewsets
from server.models import Materia

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ("descripcion",)

class MateriaView(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
