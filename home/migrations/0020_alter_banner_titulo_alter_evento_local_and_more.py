# Generated by Django 4.1.13 on 2024-07-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_banner_titulo_alter_evento_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='titulo',
            field=models.CharField(default='Banner 2024-07-02 17:24:20.073260+00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, default='Local 2024-07-02 17:24:20.073260+00:00', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(default='Evento 2024-07-02 17:24:20.073260+00:00', max_length=100),
        ),
    ]