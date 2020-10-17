from django import forms

from .models import Pedido

class VisualizarPedidoForm(forms.ModelForm):

    #Construtor utilizado para poder passar parametros da view para o form
    def __init__(self, *args, **kwargs):
        id = int(kwargs.pop('pedido_id'))
        super(VisualizarPedidoForm, self).__init__(*args, **kwargs)
    
        id_pedido = forms.IntegerField(required = False, widget=forms.HiddenInput())
        valor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Valor')
        parcela = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Parcelas')
        forma_pagamento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Forma de pagamento')
        status_pedido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Status')
        data_pedido = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}), label='Data')

        consumidor_id_consumidor = forms.ModelChoiceField(queryset = Pedido.objects.filter(pk=id))
        cliente_id_cliente = forms.ModelChoiceField(queryset = Pedido.objects.filter(pk=id))
        
        produtos = forms.ModelMultipleChoiceField(Pedido.objects.get(pk = id).produtos.all())

    class Meta:
        model = Pedido
        fields = {'id_pedido', 'valor', 'parcela', 'forma_pagamento', 'status_pedido', 'data_pedido',
                    'consumidor_id_consumidor', 'cliente_id_cliente', 'produtos'}
    