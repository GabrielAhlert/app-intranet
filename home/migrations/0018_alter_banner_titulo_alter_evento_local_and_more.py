# Generated by Django 4.1.2 on 2024-06-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_banner_titulo_alter_evento_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='titulo',
            field=models.CharField(default='Banner 2024-06-13 17:03:32.804180+00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(default='Local 2024-06-13 17:03:32.804180+00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(default='Evento 2024-06-13 17:03:32.804180+00:00', max_length=100),
        ),
    ]
