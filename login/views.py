from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from base.models import Cliente, Consumidor


class LogarView(generic.View):
    def post(self, request):
        form_email = request.POST['email']
        form_senha = request.POST['senha']

        logado = False
        #Tenta logar como cliente caso nao consiga tenta logar como consumidor
        try:
            logado = Cliente.objects.get(email=form_email, senha=form_senha)
        except:
            try:
                logado = Consumidor.objects.get(email=form_email, senha=form_senha)
            except:
                #Se nao conseguir logar, retorna a pagina de login e exibi uma error message
                return render(request, 'login/logar.html', {'error_message': 'Login inválido. Tente novamente'})
        context = {'logado': logado}
        return render(request, 'base/index.html', context)

    def get(self, request):
        return render(request, 'login/logar.html', {})

class DeslogarView(generic.View):
    def get(self, request):
        logado = False
        return render(request, 'base/index.html',{})
