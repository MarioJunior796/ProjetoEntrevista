from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=100)
    veiculo = models.CharField(max_length=100)
    trocaDeOleo = models.FloatField()

class Motorista(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=14)
    cnh = models.CharField(max_length=10)