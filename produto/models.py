from django.db import models

from cliente.models import Cliente

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    codigo_interno = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    categoria = models.CharField(max_length=20, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        
        db_table = 'produto'

    def __str__(self):
        return self.nome