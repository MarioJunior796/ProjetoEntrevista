from django.contrib import admin
from .models import controleEntradas

class ListandoCadastros(admin.ModelAdmin):
    list_display = ('id', 'dataSaida', 'horaSaida', 'kmSaida', 'destino')

admin.site.register(controleEntradas, ListandoCadastros)