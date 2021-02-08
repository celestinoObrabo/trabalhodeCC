from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Curso"

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Categoria"

class Orientacao(models.Model):
    name = models.CharField('Nome da Orientação(orientandos)', max_length=100)
    description = models.TextField('Descrição do Trabalho', blank=True)
    start_date = models.DateField('Data de início', null=True, blank=True)
    #image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    user = models.ManyToManyField(User, related_name='usuarios', blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria', null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso', null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


