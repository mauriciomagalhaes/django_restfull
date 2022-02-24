from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecosSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from comentarios.api.serializers import ComentariosSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecosSerializer()
    avaliacoes = AvaliacoesSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'atracoes', 'avaliacoes', 'comentarios', 'endereco')
        """ fields = '__all__' """