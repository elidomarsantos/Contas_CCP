# Generated by Django 4.0.5 on 2023-02-17 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0012_alter_gerais_data_do_fechamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gerais',
            name='data_do_Fechamento',
        ),
    ]