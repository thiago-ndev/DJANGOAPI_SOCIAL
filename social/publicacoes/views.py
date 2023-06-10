from rest_framework.generics import get_object_or_404
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from .models import *
from .util import cripty_senha

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
    serializer_class = PublicaoSerializer

class PublicacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacao.objects.all()
    serializer_class = PublicaoSerializer

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

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        senha = request.data['senha']
        senha = cripty_senha(senha)
        request.data['senha'] = senha
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers= headers)

    @action(methods=['get'], detail=True)
    def publicacoes(self, request, pk=None):
        usuario = self.get_object()
        serializer = PublicaoSerializer(usuario.publicacoes.all(), many=True)
        return Response(serializer.data)
        pass

    # quando for serializar, se for buscar uma coleção(varios itens) tem que ter o parametro many=True
    @action(methods=['get'], detail=True, url_path='publicacao/(?P<codigo>\d+)')
    def publicacao(self, request, codigo, pk=None):
        usuario = Usuario.objects.get(pk=pk)
        publicacao = Publicacao.objects.filter(usuario=usuario, pk = codigo).first()
        if publicacao is not None:
            serializer = PublicaoSerializer(publicacao)
            return Response(serializer.data)

        return Response(status=status.HTTP_204_NO_CONTENT)


class PublicacaoViewset(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicaoSerializer
class ComentarioViewset(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
class ReacaoViewset(viewsets.ModelViewSet):
    queryset = Reacao.objects.all()
    serializer_class = ReacaoSerializer
class ReacaoPublicadaViewset(viewsets.ModelViewSet):
    queryset = ReacaoPublicada.objects.all()
    serializer_class = ReacaoPublicadaSerializer




