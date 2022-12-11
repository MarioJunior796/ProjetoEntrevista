# Generated by Django 4.1.4 on 2022-12-09 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='controleEntradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataSaida', models.DateField()),
                ('horaSaida', models.TimeField()),
                ('kmSaida', models.FloatField()),
                ('destino', models.CharField(max_length=100)),
                ('dataRetorno', models.DateField()),
                ('horaRetorno', models.TimeField()),
                ('kmRetorno', models.FloatField()),
                ('kmPercorrido', models.FloatField()),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.motorista')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.veiculo')),
            ],
        ),
    ]
