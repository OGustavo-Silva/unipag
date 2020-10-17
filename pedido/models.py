from django.db import models

from cliente.models import Cliente
from consumidor.models import Consumidor
from produto.models import Produto

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    parcela = models.CharField(max_length=2, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=15, blank=True, null=True)
    status_pedido = models.CharField(max_length=20, blank=True, null=True)
    data_pedido = models.DateField(blank=True, null=True)
    consumidor_id_consumidor = models.ForeignKey(Consumidor, models.DO_NOTHING, db_column='consumidor_id_consumidor')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    produtos = models.ManyToManyField(Produto)

    class Meta:
        
        db_table = 'pedido'
