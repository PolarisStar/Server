from .models import Perrito, Usuario
from rest_framework import serializers

class PerritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perrito
        fields = ('imagen','nombre', 'raza', 'descripcion', 'estado')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username','password', 'admin')

