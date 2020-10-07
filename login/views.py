from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from base.models import Cliente, Consumidor
from base.views import carregarUser




class LogarView(generic.View):    
    def post(self, request):
        form_email = request.POST['email']
        form_senha = request.POST['senha']

        #Tenta logar como cliente caso nao consiga tenta logar como consumidor
        try:
            request.session['id_logado'] = Cliente.objects.get(email=form_email, senha=form_senha).id_cliente
        except:
            try:
                request.session['id_logado'] = Consumidor.objects.get(email=form_email, senha=form_senha).id_consumidor
            except:
                #Se nao conseguir logar, retorna a pagina de login e exibi uma error message
                return render(request, 'login/logar.html', {'error_message': 'Login inválido. Tente novamente'})

        logado = carregarUser(request.session['id_logado'])
        return render(request, 'base/index.html', {'logado': logado})

    

    def get(self, request):
        return render(request, 'login/logar.html', {})

class DeslogarView(generic.View):
    def get(self, request):
        request.session['id_logado'] = 0
        return render(request, 'base/index.html',{})
