from django.db import models
from orientacao.models import Orientacao

class Encontros(models.Model):
    titulo = models.CharField('Título do encontro', max_length=255)
    descricao = models.TextField('Descrição breve do encontro', blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    orientacao = models.ForeignKey(Orientacao, on_delete=models.CASCADE,verbose_name='Orientação:',null = True)
    start_date = models.DateTimeField('Data da reunião', null=True, blank=True)
    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ['created_at']
