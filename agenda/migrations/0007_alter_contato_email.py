# Generated by Django 4.1.2 on 2024-05-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_alter_funcao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
