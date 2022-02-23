from django import views
from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register('pontoturistico', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
