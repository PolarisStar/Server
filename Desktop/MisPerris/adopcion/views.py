from rest_framework import generics
from .models import Perrito, Usuario
from .serializers import PerritoSerializer, UsuarioSerializer
from django.shortcuts import render, get_object_or_404

class PerritoList(generics.ListCreateAPIView):
    queryset = Perrito.objects.all()
    serializer_class = PerritoSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

class UsuarioRegister(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj