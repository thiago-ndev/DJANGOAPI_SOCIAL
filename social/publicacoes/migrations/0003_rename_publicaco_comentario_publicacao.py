# Generated by Django 3.2.19 on 2023-06-01 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicacoes', '0002_alter_publicacao_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='publicaco',
            new_name='publicacao',
        ),
    ]
