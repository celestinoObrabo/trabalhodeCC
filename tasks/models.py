from django.db import models
from django.urls import reverse


from orientacao.models import Orientacao


class Task(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    orientacao = models.ForeignKey(Orientacao, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField('Data de Entrega', null = True, blank = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("task-list",kwargs = {"id":self.orientacao})

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task.title

class Arquivos(models.Model):
    name = models.CharField('Nome do que esta enviando',max_length=100)
    arquivo = models.FileField(upload_to='')
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField('Enviado em: ',auto_now_add=True)
    def __str__(self):
        return self.name






