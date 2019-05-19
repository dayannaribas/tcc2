# Generated by Django 2.1 on 2019-05-19 01:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='broker',
            field=models.CharField(default='', help_text='Numero do IP do servidor MQTT. Ex: 192.168.100.107', max_length=13, validators=[django.core.validators.validate_ipv4_address], verbose_name='Broker:'),
        ),
    ]