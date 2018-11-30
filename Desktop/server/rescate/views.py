from .models import Perrito
from rest_framework import viewsets
from rescate.serializers import PostSerializer

class PostViewSet( viewsets.ModelViewSet ):
    queryset = Perrito.objects.all().order_by( 'nombrePerro' )
    serializer_class = PostSerializer