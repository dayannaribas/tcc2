# Generated by Django 2.1 on 2019-05-20 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_mensagem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mensagem',
            new_name='Ligacao',
        ),
        migrations.AlterModelOptions(
            name='ligacao',
            options={'verbose_name': 'Ligação', 'verbose_name_plural': 'Ligações'},
        ),
    ]
