from django import views
from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentariosViewSet
from enderecos.api.viewsets import EnderecosViewSet

router = routers.DefaultRouter()
router.register('pontoturistico', PontoTuristicoViewSet)
router.register('atracoes', AtracaoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('comentarios', ComentariosViewSet)
router.register('enderecos', EnderecosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
