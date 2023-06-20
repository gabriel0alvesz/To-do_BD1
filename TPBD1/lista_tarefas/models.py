from typing import Literal
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class Convite(models.Model):
    id_convite = models.AutoField(primary_key=True)
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

class MeuUsuarioManager(BaseUserManager):
    def create_user(self, nome_usuario, senha=None, email='', nome='', telefone=''):
        if not nome_usuario:
            raise ValueError('O nome de usuário deve ser definido')

        if not email:
            raise ValueError('O email deve ser definido')

        if not nome:
            raise ValueError('O nome deve ser definido')

        if not telefone:
            raise ValueError('O telefone deve ser definido')

        user = self.model(nome_usuario=nome_usuario, email=email, nome=nome, telefone=telefone)
        user.set_password(senha)
        print(len(user.password))
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    nome_usuario = models.CharField(primary_key=True, max_length=20)
    nome = models.CharField(max_length=60)
    telefone = models.IntegerField()
    email = models.CharField(max_length=60)
    last_login = None

    [field for field in AbstractBaseUser._meta.fields if field.name == "password"][0].db_column = "senha"

    objects = MeuUsuarioManager()

    USERNAME_FIELD = 'nome_usuario'
    REQUIRED_FIELDS = ['email', 'nome','telefone']

    def __str__(self):
        return self.nome_usuario

    @property
    def is_anonymous(self) -> Literal[False]:
        return super().is_anonymous

    class Meta:
        managed = False
        db_table = 'Usuario'
