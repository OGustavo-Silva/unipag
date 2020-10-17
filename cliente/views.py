from django.shortcuts import render
from django.views import generic

from .models import Cliente

from base.views import estaLogado, carregarUser
from pedido.models import Pedido

class HomeCliente(generic.View):
    template_name = 'cliente/homecliente.html'

    @estaLogado
    def get(self, request):
        id = request.session['id_logado']

        pedido = Pedido.objects.filter(cliente_id_cliente = id)
        logado = carregarUser(request, id)

        context = {'logado': logado, 'pedido': pedido}
        return render(request, self.template_name, context)
