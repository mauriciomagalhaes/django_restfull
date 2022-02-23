import re
from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios, blank=True)
    avaliacoes = models.ManyToManyField(Avaliacoes, blank=True)

    def __str__(self):
        return self.nome
        
     