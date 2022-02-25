from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import PontoTuristico
from enderecos.models import Enderecos
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecosSerializer
#from avaliacoes.api.serializers import AvaliacoesSerializer
#from comentarios.api.serializers import ComentariosSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)         #netest fields
    endereco = EnderecosSerializer()                #netest fields
    descricao_completa = SerializerMethodField()    #netest fields
    #avaliacoes = AvaliacoesSerializer(many=True)   #netest fields
    #comentarios = ComentariosSerializer(many=True) #netest fields

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'atracoes', 'avaliacoes', 'comentarios', 'endereco', 'descricao_completa', 'descricao_completa2')
        read_only_fields = ('comentarios', 'avaliacoes')
       # fields = '__all__'

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
    
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Enderecos.objects.create(**endereco)
        ponto.endereco = end      
        
        ponto.save()

        return ponto

    def get_descricao_completa(self, obj): # incluindo  serializacao por aqui
        return '%s - %s' % (obj.nome, obj.descricao)


    