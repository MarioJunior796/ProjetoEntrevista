from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from controleEntradas.models import controleEntradas
from .models import Veiculo, Motorista

def index(request):

    veiculos = controleEntradas.objects.order_by('-dataSaida').all()

    dados = {
        'veiculos': veiculos
    }

    return render(request, 'index.html', dados)

def detalhes(request, veiculoId):
    veiculo = get_object_or_404(controleEntradas, pk=veiculoId)

    dados = {
        'veiculo': veiculo
    }

    return render(request, '../templates/detalhes.html', dados)

def cadastroVeiculo(request):

    if request.method == 'POST':
        placa = request.POST['placa']
        marca = request.POST['marca']
        veiculo = request.POST['veiculo']
        trocaDeOleo = request.POST['trocaOleo']

        if campo_vazio(placa):
            messages.error(request, 'O campo placa nao pode ser nulo')
            redirect('cadastroVeiculo')

        if campo_vazio(marca):
            messages.error(request, 'O campo marca nao pode ser nulo')
            redirect('cadastroVeiculo')

        if campo_vazio(veiculo):
            messages.error(request, 'O campo veiculo nao pode ser nulo')
            redirect('cadastroVeiculo')

        veiculo = Veiculo.objects.create(placa=placa, marca=marca, veiculo=veiculo, trocaDeOleo=trocaDeOleo)
        veiculo.save()
        print('veiculo cadastrado com sucesso')
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('cadastroVeiculo')

    return render(request, '../templates/cadastroVeiculo.html')

def cadastroMotorista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        cnh = request.POST['cnh']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome nao pode ser nulo')
            redirect('cadastroMotorista')

        if campo_vazio(telefone):
            messages.error(request, 'O campo telefone nao pode ser nulo')
            redirect('cadastroMotorista')

        if campo_vazio(cnh):
            messages.error(request, 'O campo cnh nao pode ser nulo')
            redirect('cadastroMotorista')

        motorista = Motorista.objects.create(nome=nome, telefone=telefone, cnh=cnh)
        motorista.save()
        print('Motorista cadastrado com sucesso')
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('cadastroMotorista')
    else:
        return render(request, '../templates/cadastroMotorista.html')

def buscar(request):

    listaVeiculos = controleEntradas.objects.order_by('-dataSaida').filter()

    if 'buscar' in request.GET:
        nomeBuscar = request.GET['buscar']
        if buscar:
            lista_veiculos = listaVeiculos.filter(dataSaida__icontains=nomeBuscar)

    dados = {
        'veiculos' : lista_veiculos
    }

    return render(request, 'buscar.html', dados)

def campo_vazio(campo):
    return not campo.strip()

def deletarVeiculo(request, veiculoId):
    veiculo = get_object_or_404(controleEntradas, pk=veiculoId)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('index')
    return render(request, 'deleteConfirmacao.html')

def editarVeiculo(request, veiculoId):
    veiculo = get_object_or_404(controleEntradas, pk=veiculoId)
    veiculoEditar = { 'veiculo': veiculo }
    return render(request, '../templates/editarControleVeiculo.html', veiculoEditar)

def atualizarVeiculo(request):
    if request.method == 'POST':
        veiculoId = request.POST['veiculoId']
        v = controleEntradas.objects.get(pk=veiculoId)
        v.dataSaida = request.POST['dataSaida']
        v.horaSaida = request.POST['horaSaida']
        v.kmSaida = request.POST['kmSaida'].replace(",", ".")
        v.destino = request.POST['destino']
        v.dataRetorno = request.POST['dataRetorno']
        v.horaRetorno = request.POST['horaRetorno']
        v.kmRetorno = request.POST['kmRetorno'].replace(",", ".")
        v.kmPercorrido = request.POST['kmPercorrido'].replace(",", ".")

        if(float(v.veiculo.trocaDeOleo) < float(v.kmRetorno)):
            messages.error(request, 'É preciso realizar a troca de óleo')

        v.save()
        return redirect('index')