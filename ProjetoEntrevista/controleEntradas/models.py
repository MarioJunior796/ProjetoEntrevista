from django.db import models
from cadastro.models import Veiculo, Motorista

class controleEntradas(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    dataSaida = models.DateField()
    horaSaida = models.TimeField()
    kmSaida = models.FloatField()
    destino = models.CharField(max_length=100)
    dataRetorno = models.DateField()
    horaRetorno = models.TimeField()
    kmRetorno = models.FloatField()
    kmPercorrido = models.FloatField()
    
        
    
