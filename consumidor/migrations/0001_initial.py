# Generated by Django 3.1 on 2020-10-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('id_consumidor', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=40)),
                ('sobrenome', models.CharField(max_length=60)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('senha', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=1)),
                ('logradouro', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('complemento', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_cartao', models.CharField(blank=True, max_length=16, null=True)),
                ('codigo_seguranca', models.CharField(blank=True, max_length=3, null=True)),
                ('titular_cartao', models.CharField(blank=True, max_length=60, null=True)),
                ('validade_cartao', models.DateField(blank=True, null=True)),
                ('limite_compra', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'consumidor',
            },
        ),
    ]