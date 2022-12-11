from django.contrib import admin
from .models import Veiculo, Motorista

class ListandoVeiculo(admin.ModelAdmin):
    list_display = ('id', 'placa', 'marca', 'veiculo', 'trocaDeOleo')
    list_display_links = ('id', 'placa')
    search_fields = ('placa', )
    list_filter = ('marca',)
    list_per_page = 10

class ListandoMotorista(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'cnh')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 10

admin.site.register(Veiculo, ListandoVeiculo)
admin.site.register(Motorista, ListandoMotorista)