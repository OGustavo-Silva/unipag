# Generated by Django 3.1 on 2020-10-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=17, unique=True)),
                ('email', models.CharField(max_length=80)),
                ('telefone', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=255)),
                ('logradouro', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('complemento', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]