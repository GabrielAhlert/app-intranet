# Generated by Django 4.1.1 on 2022-10-06 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('funcao', models.CharField(max_length=64)),
                ('ramal', models.CharField(max_length=16)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=100)),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='agenda.unidade')),
            ],
        ),
    ]