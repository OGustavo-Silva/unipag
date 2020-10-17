# Generated by Django 3.1 on 2020-10-12 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumidor', '0001_initial'),
        ('cliente', '0001_initial'),
        ('base', '0002_auto_20200930_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enderecoentrega',
            name='id_consumidor',
            field=models.ForeignKey(db_column='id_consumidor', on_delete=django.db.models.deletion.DO_NOTHING, to='consumidor.consumidor'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente_id_cliente',
            field=models.ForeignKey(db_column='cliente_id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='consumidor_id_consumidor',
            field=models.ForeignKey(db_column='consumidor_id_consumidor', on_delete=django.db.models.deletion.DO_NOTHING, to='consumidor.consumidor'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id_cliente',
            field=models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Consumidor',
        ),
    ]
