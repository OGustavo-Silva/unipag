from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from cliente.models import Cliente
from cliente.forms import PerfilClienteForm

from consumidor.models import Consumidor
from consumidor.forms import PerfilConsumidorForm


def carregarUser(request, id):
        email_logado=request.session['email_logado']
        logado = False
        try:
            logado = Cliente.objects.get(email=email_logado, id_cliente=id)
        except:
            try:
                logado = Consumidor.objects.get(email=email_logado, id_consumidor=id)
            except e:
                print('Erro try carregaUser\n', e)
        finally:
            return logado

class IndexView(generic.View):
    template_name = 'base/index.html'

    def get(self, request):
        logado = False
        if request.session['id_logado'] != 0:
            try:
                id = request.session['id_logado']
                logado = carregarUser(request, id)
            except e:
                print('Index Try logar\n', e)
        context = {'logado':logado}

        return render(request, self.template_name, context)

#Decorator
def estaLogado(my_view):
    def verifica(self, request, *args, **kwargs):
        id_logado = request.session['id_logado']
        if id_logado != 0:
            return my_view(self, request, *args, **kwargs)
        else:
            return render(request, 'login/logar.html', {'error_message': 'Você precisa estar logado.'})
    return verifica


class MeuPerfilView(generic.TemplateView):
    template_name = 'base/meuperfil.html'

    @estaLogado
    def get(self, request,logado_tipo):

        if logado_tipo == 'cliente':
            logado = Cliente.objects.get(id_cliente=request.session['id_logado'])
            form_class = PerfilClienteForm(instance=logado)
        else:
            logado = Consumidor.objects.get(id_consumidor=request.session['id_logado'])
            form_class = PerfilConsumidorForm(instance=logado)
            
        context = {'logado':logado, 'form':form_class}

        return render(request, self.template_name, context)

