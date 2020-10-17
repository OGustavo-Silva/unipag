from django.db import models

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

    def __str__(self):
        return 'Consumidor ' + self.nome
