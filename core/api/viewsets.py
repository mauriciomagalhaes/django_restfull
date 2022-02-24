
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()
"""     
    def list(self, request, *args, **kwargs):
        return super(PontoTuristico, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristico, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristico, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristico, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristico, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristico, self).partial_update(request, *args, **kwargs) """
    
    