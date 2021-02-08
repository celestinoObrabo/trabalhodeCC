from django.contrib import admin

from .models import Task,Comment,Arquivos

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Arquivos)
