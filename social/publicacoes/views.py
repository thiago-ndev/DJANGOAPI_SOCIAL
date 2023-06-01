from rest_framework.generics import get_object_or_404
from rest_framework import generics
from django.shortcuts import render
from .models import *
from .serializers import *


# Create your views here.
# endpoints


# ENDPOINT -> POST, GET, DELETE, UPDATE, PATCH
# listCreate -> lista / create (post).

class UsuariosAPIView(generics.ListCreateAPIView):
    # query all
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PublicacoesAPIView(generics.ListCreateAPIView):
    queryset = Publicacao.objects.all()
    serializer_class = PublicaSerializer

class PublicacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacao.objects.all()
    serializer_class = PublicaSerializer

class ComentariosAPIView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ReacoesAPIView(generics.ListCreateAPIView):
    queryset = Reacao.objects.all()
    serializer_class = ReacaoSerializer

class ReacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reacao.objects.all()
    serializer_class = ReacaoSerializer

class ReacoesPublicadasAPIView(generics.ListCreateAPIView):
    queryset = ReacaoPublicada.objects.all()
    serializer_class = ReacaoPublicadaSerializer


class ReacaoPublicadaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReacaoPublicada.objects.all()
    serializer_class = ReacaoPublicadaSerializer



