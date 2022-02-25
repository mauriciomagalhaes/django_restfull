from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from enderecos.models import Enderecos
# Create your models here.

class DocIdentificacao(models.Model):
    description = models.CharField(max_length=100)

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacoes, blank=True)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField('DocIdentificacao', on_delete=models.CASCADE, null=True, blank=True)

    @property # incluindo  serializacao por aqui
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome
        
     