# Generated by Django 4.1.2 on 2024-05-31 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_rename_is_active_categoria_categoria_ativa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='profundidade',
        ),
    ]
