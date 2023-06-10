from django.urls import path
from .views import *
from rest_framework_nested.routers import SimpleRouter

app_name = 'publicacoes'

router = SimpleRouter()

router.register('usuarios', UsuarioViewset)
router.register('publicacoes',PublicacaoViewset)
router.register('comentarios',ComentarioViewset)
router.register('reacao',ReacaoViewset)
router.register('reacaopublicada',ReacaoPublicadaViewset)

urlpatterns = [
    path('usuarios/', UsuariosAPIView.as_view(), name='usuarios'),
    path('usuarios/<int:pk>', UsuarioAPIView.as_view(), name='usuario'),

    path('publicacoes/', PublicacoesAPIView.as_view(), name='publicacoes'),
    path('publicacoes/<int:pk>', PublicacaoAPIView.as_view(), name='publicacao'),

    path('comentarios/', ComentariosAPIView.as_view(), name='comentarios'),
    path('comentario/<int:pk>', ComentarioAPIView.as_view(), name='comentario'),

    path('reacoes/', ReacoesAPIView.as_view(), name='reacoes'),
    path('reacoes/<int:pk>', ReacaoAPIView.as_view(), name='reacao'),

    path('reacoespublicadas/', ReacoesPublicadasAPIView.as_view(), name='reacoespublicadas'),
    path('reacoespublicadas/<int:pk>', ReacaoPublicadaAPIView.as_view(), name='reacaopublicada'),

]
