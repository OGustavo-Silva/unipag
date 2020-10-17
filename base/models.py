# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from consumidor.models import Consumidor

class EnderecoEntrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    id_consumidor = models.ForeignKey(Consumidor, models.DO_NOTHING, db_column='id_consumidor')

    class Meta:
        
        db_table = 'endereco_entrega'




