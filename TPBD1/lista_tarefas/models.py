from django.db import models

# Create your models here.

class Convite(models.Model):
    aceito = models.IntegerField()
    fk_nome_usuario_env = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_nome_usuario_env')
    fk_nome_usuario_rec = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_nome_usuario_rec', related_name='convite_fk_nome_usuario_rec_set')
    fk_lista = models.ForeignKey('ListaDeTarefas', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Convite'


class ListaDeTarefas(models.Model):
    id_lista = models.AutoField(primary_key=True)
    nome_descritivo = models.CharField(max_length=60)
    data_hora_criacao = models.DateTimeField()
    data_hora_modificacao = models.DateTimeField()
    responsavel_modificacao = models.CharField(max_length=20)
    fk_nome_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_nome_usuario')

    class Meta:
        managed = False
        db_table = 'Lista_de_Tarefas'


class Tarefas(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField()
    data_vencimento = models.DateTimeField(blank=True, null=True)
    tarefa_concluida = models.IntegerField()
    fk_lista = models.ForeignKey(ListaDeTarefas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Tarefas'


class Usuario(models.Model):
    nome_usuario = models.CharField(primary_key=True, max_length=20)
    senha = models.CharField(max_length=64)
    nome = models.CharField(max_length=60)
    telefone = models.IntegerField()
    email = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'Usuario'
