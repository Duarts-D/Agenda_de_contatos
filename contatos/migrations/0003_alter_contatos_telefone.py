# Generated by Django 4.1.5 on 2023-01-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contatos_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
