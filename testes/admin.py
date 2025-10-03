from django.contrib import admin
from .models import Teste, Resposta


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo']
    list_filter = ['tipo']


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['email', 'teste', 'pago', 'criado_em']
    list_filter = ['pago', 'teste']
    search_fields = ['email']
