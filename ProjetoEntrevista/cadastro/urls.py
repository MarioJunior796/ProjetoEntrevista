from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:veiculoId>', views.detalhes, name='detalhes'),
  path('cadastroVeiculo', views.cadastroVeiculo, name='cadastroVeiculo'),
  path('cadastroMotorista', views.cadastroMotorista, name='cadastroMotorista'),
  path('buscar', views.buscar, name='buscar'),
  path('deleta/<int:veiculoId>', views.deletarVeiculo, name='deletarVeiculo'),
  path('edita/<int:veiculoId>', views.editarVeiculo, name='editarVeiculo'),
  path('atualizaVeiculo', views.atualizarVeiculo, name='atualizarVeiculo')
]
