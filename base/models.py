# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=17)
    email = models.CharField(max_length=80)
    telefone = models.CharField(max_length=11)
    senha = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        
        db_table = 'cliente'

    def tipo(self):
        return 'cliente'


class Consumidor(models.Model):
    id_consumidor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=60)
    email = models.CharField(max_length=50, blank=True, null=True)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(unique=True, max_length=11)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    logradouro = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    nacionalidade = models.CharField(max_length=20, blank=True, null=True)
    numero_cartao = models.CharField(max_length=16, blank=True, null=True)
    codigo_seguranca = models.CharField(max_length=3, blank=True, null=True)
    titular_cartao = models.CharField(max_length=60, blank=True, null=True)
    validade_cartao = models.DateField(blank=True, null=True)
    limite_compra = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        
        db_table = 'consumidor'

    def tipo(self):
        return 'consumidor'


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


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    parcela = models.CharField(max_length=2, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=15, blank=True, null=True)
    status_pedido = models.CharField(max_length=20, blank=True, null=True)
    data_pedido = models.DateField(blank=True, null=True)
    consumidor_id_consumidor = models.ForeignKey(Consumidor, models.DO_NOTHING, db_column='consumidor_id_consumidor')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')

    class Meta:
        
        db_table = 'pedido'


class PedidoProduto(models.Model):
    quantidade = models.IntegerField()
    id_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='id_produto')
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')

    class Meta:
        
        db_table = 'pedido_produto'


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    codigo_interno = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    categoria = models.CharField(max_length=20, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        
        db_table = 'produto'
