# Generated by Django 4.1.2 on 2024-06-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='titulo',
            field=models.CharField(default='Banner 2024-06-01 00:45:22.145001+00:00', max_length=100),
        ),
    ]
