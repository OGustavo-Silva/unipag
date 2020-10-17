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

    def __str__(self):
        return 'Cliente ' + self.razao_social
