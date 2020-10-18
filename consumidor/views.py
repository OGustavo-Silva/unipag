from django.shortcuts import render
from django.views import generic

from .models import Consumidor
from base.views import estaLogado, carregarUser
from pedido.models import Pedido

class homeConsumidor(generic.View):
    template_name = 'consumidor/homeconsumidor.html'

    @estaLogado
    def get(self, request):
        search = request.GET.get('search')
        id = request.session['id_logado']

        if search:
            pedido = Pedido.objects.filter(data_pedido__icontains=search, consumidor_id_consumidor = id)|Pedido.objects.filter(valor__icontains=search,consumidor_id_consumidor = id)

        else:
            pedido = Pedido.objects.filter(consumidor_id_consumidor = id)

        logado = carregarUser(request, id)

        context = {'pedido': pedido, 'logado': logado}
        return render(request, self.template_name, context)