# Generated by Django 4.1.2 on 2022-10-31 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_funcao_alter_contato_funcao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcao',
            options={'verbose_name': 'Funcão', 'verbose_name_plural': 'Funções'},
        ),
    ]