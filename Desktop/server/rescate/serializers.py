from .models import Perrito
from rest_framework import serializers

class PostSerializer( serializers.HyperlinkedModelSerializer ):
    class Meta:
        model = Perrito
        fields = ( 'nombrePerro', 'razaP', 'descripcion', 'imagen', 'estado' )