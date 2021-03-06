from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from cliente.models import Cliente
from consumidor.models import Consumidor

from cliente.forms import CadastroClienteForm
from consumidor.forms import CadastroConsumidorForm

class CadastrarCliente(generic.View):
    def post(self, request):
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login/logar.html')
        return render(request, 'cadastro/cadastrarcliente.html', {'error_message': 'Não foi possível efetuar o cadastro'})

    def get(self, request):
        form = ClienteForm()
        return render(request, 'cadastro/cadastrarcliente.html', {'form':form})

class CadastrarConsumidor(generic.View):
    def post(self, request):
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login/logar.html')
        return render(request, 'cadastro/cadastrarconsumidor.html', {'error_message': 'Não foi possível efetuar o cadastro'})

    def get(self, request):
        form = ConsumidorForm()
        return render(request, 'cadastro/cadastrarconsumidor.html', {'form': form})
