from rest_framework import serializers
from .models import *

class Login(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('email', 'senha')

class LoginAcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAcesso
        fields = ('codigo', 'codigoUsuario', 'dataAcesso')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

        # informa que as publicacoes é apenas para saida
        # para não ter que cadastrar uma publicacao em usuario que ainda nao tem cadastro

        read_only_fields = ['publicacoes']

        #tudo dentro field é trado como entrada e saida de dados
        fields = ('codigo', 'nome', 'email', 'publicacoes', 'senha', 'logado', 'ativo')

        # definir os niveis de prioridades do serializador
        # tomar cuidado, pois isso pode virar uma consulta ciclica

        depth = 1

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('codigo', 'nome', 'comentario', 'dataComentario', 'ativo')

class PublicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = ('codigo', 'texto', 'fotoUrl', 'usuario')


class ReacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reacao
        fields = ('codigo', 'tipo', 'descricao')


class ReacaoPublicadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReacaoPublicada
        fields = ('codigo', 'nome', 'publicacao', 'reacao', 'dataReacao')
