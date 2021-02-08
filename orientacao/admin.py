from django.contrib import admin
from .models import Orientacao, Categoria , Curso


class OrientacaoAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'created_at']
    search_fields = ['name']


admin.site.register(Orientacao, OrientacaoAdmin),
admin.site.register(Categoria),
admin.site.register(Curso),

