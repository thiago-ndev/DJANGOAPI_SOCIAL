# Generated by Django 3.2.19 on 2023-05-31 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=200)),
                ('fotoUrl', models.CharField(default='vazio', max_length=200)),
            ],
            options={
                'verbose_name': 'Publicacao',
                'verbose_name_plural': 'Publicacoes',
                'db_table': 'publicacoes',
            },
        ),
        migrations.CreateModel(
            name='Reacao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField()),
                ('descricao', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Reacao',
                'verbose_name_plural': 'Reacoes',
                'db_table': 'reacao',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuario',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='ReacaoPublicada',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('dataReacao', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(default='Sem Nome', max_length=100)),
                ('publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacoes.publicacao')),
                ('reacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicacoes.reacao')),
            ],
            options={
                'verbose_name': 'Reacao_Publicada',
                'verbose_name_plural': 'Reacoes_Publicadas',
                'db_table': 'reacao_publicada',
            },
        ),
        migrations.AddField(
            model_name='reacao',
            name='publicacoes',
            field=models.ManyToManyField(through='publicacoes.ReacaoPublicada', to='publicacoes.Publicacao'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='reacaoes',
            field=models.ManyToManyField(through='publicacoes.ReacaoPublicada', to='publicacoes.Reacao'),
        ),
        migrations.AddField(
            model_name='publicacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicacoes', to='publicacoes.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=200)),
                ('dataComentario', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('publicaco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='publicacoes.publicacao')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'comentario',
            },
        ),
    ]
