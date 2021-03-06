from rest_framework import serializers, viewsets
from server.models import Nacionalidad

class NacionalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = ('gentilicio', 'nombre',)


class NacionalidadView(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = NacionalidadSerializer
