from rest_framework.serializers import ModelSerializer, SerializerMethodField
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
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'foto', 'atracoes', 'avaliacoes', 'comentarios', 'endereco', 'descricao_completa', 'descricao_completa2'
            )
        """ fields = '__all__' """
    
    def get_descricao_completa(self, obj): # incluindo  serializacao por aqui
        return '%s - %s' % (obj.nome, obj.descricao)    

    