from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'texto', 'fotoUrl', 'usuario')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'comentario', 'dataComentario', 'ativo', 'publicacao')

@admin.register(Reacao)
class ReacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')

@admin.register(ReacaoPublicada)
class ReacaoPublicadaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'publicacao', 'reacao', 'dataReacao')
