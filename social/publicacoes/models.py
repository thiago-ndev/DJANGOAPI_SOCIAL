from django.db import models

# Create your models here.

class Login:
    def __init__(self, email=None, senha=None):
        self.email = email
        self.senha = senha

    def __str__(self):
        return '{}, {}'.format(self.senha, self.email)

    def __repr__(self):
        return '{}, {}'.format(self.senha, self.email)


class LogAcesso(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigoUsuario = models.IntegerField(null=False)
    dataAcesso = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.codigoUsuario, self.dataAcesso)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.codigoUsuario, self.dataAcesso)



class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(null=False, max_length=100)
    email = models.CharField(null=False, unique=True, max_length=50)

    senha = models.CharField(null=False, max_length=255, default='vazio')
    ativo = models.BooleanField(null=False, default=True)
    logado = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = "usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return '{}, {}, {}, {}, {},{}'.format(self.codigo, self.nome, self.email,
                                              self.senha, self.ativo, self.logado)

    def __repr__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.codigo, self.nome, self.email,
                                               self.senha, self.ativo, self.logado)

class Publicacao(models.Model):

    codigo = models.AutoField(primary_key=True)
    texto = models.CharField(null=False, max_length=200)
    fotoUrl = models.CharField(null=False, default='vazio', max_length=200)

    usuario = models.ForeignKey(Usuario, related_name='publicacoes', on_delete=models.CASCADE)

    reacoes = models.ManyToManyField('Reacao', through='ReacaoPublicada')

    class Meta:
        db_table = 'publicacao'
        verbose_name = 'Publicacao'
        verbose_name_plural = 'Publicacoes'

    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.texto, self.fotoUrl)

    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.texto, self.fotoUrl)




class Comentario(models.Model):
    codigo = models.AutoField(primary_key = True)
    nome = models.CharField(null=False, max_length=100)
    comentario = models.CharField(null=False, max_length=200)
    dataComentario= models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    publicacao = models.ForeignKey(Publicacao, related_name="comentarios", on_delete=models.CASCADE)

    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.codigo, self.nome, self.comentario,
                                           self.dataComentario, self.ativo)

    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(self.codigo, self.nome, self.comentario,
                                           self.dataComentario, self.ativo)


class Reacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.IntegerField(null=False)
    descricao = models.CharField(null=False, max_length=20)

    publicacoes = models.ManyToManyField(Publicacao,  through='ReacaoPublicada')

    class Meta:
        db_table = 'reacao'
        verbose_name = 'Reacao'
        verbose_name_plural = 'Reacoes'


    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.tipo, self.descricao)


    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.tipo, self.descricao)


class ReacaoPublicada(models.Model):
    codigo = models.AutoField(primary_key=True)
    dataReacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=100, null=False, default="Sem Nome")

    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)
    reacao = models.ForeignKey(Reacao, on_delete=models.CASCADE)


    class Meta:
        db_table = 'reacao_publicada'
        verbose_name = 'Reacao_Publicada'
        verbose_name_plural = 'Reacoes_Publicadas'


    def __str__(self):
        return '{}, {}, {}'.format(self.codigo, self.dataReacao, self.nome)


    def __repr__(self):
        return '{}, {}, {}'.format(self.codigo, self.dataReacao, self.nome)
