from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Pedido
from .forms import VisualizarPedidoForm

class VisualizarPedido(generic.View):
    template_name = 'pedido/visualizarpedido.html'
 
    def get(self, request, id_pedido):
        pedido = get_object_or_404(Pedido, pk=id_pedido)

        form_class = VisualizarPedidoForm(instance=pedido, pedido_id=id_pedido)

        context={'form': form_class}
        return render(request, self.template_name, context)
