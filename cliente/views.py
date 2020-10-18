from django.shortcuts import render
from django.views import generic

from .models import Cliente

from base.views import estaLogado, carregarUser
from pedido.models import Pedido

class HomeCliente(generic.View):
    template_name = 'cliente/homecliente.html'

    @estaLogado
    def get(self, request):
        search = request.GET.get('search')
        id = request.session['id_logado']

        if search:
            pedido = Pedido.objects.filter(data_pedido__icontains=search, cliente_id_cliente = id)|Pedido.objects.filter(valor__icontains=search, cliente_id_cliente = id)
        else:
            pedido = Pedido.objects.filter(cliente_id_cliente = id)
        
        logado = carregarUser(request, id)

        context = {'logado': logado, 'pedido': pedido}
        return render(request, self.template_name, context)
