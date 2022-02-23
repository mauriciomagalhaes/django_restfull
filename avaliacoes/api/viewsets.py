from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from avaliacoes.api.serializers import AvaliacoesSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer
