# Generated by Django 4.1.4 on 2022-12-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=14)),
                ('cnh', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('marca', models.CharField(max_length=100)),
                ('veiculo', models.CharField(max_length=100)),
                ('trocaDeOleo', models.FloatField()),
            ],
        ),
    ]