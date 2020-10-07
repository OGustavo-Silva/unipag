from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from .models import Cliente, Consumidor
from .forms import PerfilClienteForm


class IndexView(generic.View):
    def get(self, request):
        return render(request, 'base/index.html', {})

def carregarUser(id):
        try:
            logado = Cliente.objects.get(id_cliente=id)
        except:
            try:
                logado = Consumidor.objects.get(id_consumidor=id)
            except:
                logado=False
        return logado

#Decorator
def estaLogado(my_view):
    def verifica(self, request, *args, **kwargs):
        id_logado = request.session['id_logado']
        if id_logado != 0:
            return my_view(self, request, *args, **kwargs)
        else:
            return render(request, 'login/logar.html', {})
    return verifica


class MeuPerfilView(generic.TemplateView):
    @estaLogado
    def get(self, request):
        #template_name = 'base/meuperfil.html'
        #model = Cliente
        
        logado = carregarUser(request.session['id_logado'])
        form_class = PerfilClienteForm(instance=logado)
        context = {'logado':logado, 'form':form_class}

        return render(request, 'base/meuperfil.html', context)

