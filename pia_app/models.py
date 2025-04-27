# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgendaQuadra(models.Model):
    id_quadra = models.ForeignKey('Quadra', models.DO_NOTHING, db_column='id_quadra', blank=True, null=True)
    id_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='id_pessoa', blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    reservado = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda_quadra'


class AgendaUsuario(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    compromisso = models.CharField(max_length=200, blank=True, null=True)
    data_hora_inicio = models.DateField(blank=True, null=True)
    data_hora_fim = models.DateField(blank=True, null=True)
    id_usuario_pago = models.ForeignKey('UsuarioPago', models.DO_NOTHING, db_column='id_usuario_pago', blank=True, null=True)
    data_insert = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda_usuario'


class LocaisAtuacao(models.Model):
    id_locais_atuacao = models.AutoField(primary_key=True)
    id_usuario_pago = models.ForeignKey('UsuarioPago', models.DO_NOTHING, db_column='id_usuario_pago', blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dias_disponiveis = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    data_insert = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locais_atuacao'


class Log(models.Model):
    id_log = models.AutoField(primary_key=True)
    acao = models.CharField(max_length=10, blank=True, null=True)
    page = models.CharField(max_length=20, blank=True, null=True)
    id_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='id_pessoa', blank=True, null=True)
    data_insert = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Pessoa(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150)
    data_insert = models.DateTimeField(blank=True, null=True)
    senha = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'pessoa'


class PropietarioQuadra(models.Model):
    id = models.IntegerField(primary_key=True)
    id_pessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='id_pessoa', blank=True, null=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    data_insert = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario_quadra'


class Quadra(models.Model):
    id_propietario = models.ForeignKey(PropietarioQuadra, models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=500)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    preco_hora = models.DecimalField(max_digits=6, decimal_places=2)
    ativo = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quadra'


class UsuarioPago(models.Model):
    id_usuario_pago = models.AutoField(primary_key=True)
    id_pessoa = models.IntegerField(blank=True, null=False)
    nome = models.CharField(max_length=120, blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    preco_hora = models.CharField(max_length=100, blank=True, null=True)
    disponivel = models.CharField(max_length=100, blank=True, null=True)
   
    class Meta:
        managed = False
        db_table = 'usuario_pago'

class AgendaUsuarioPago(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    id_usuario_pago = models.IntegerField(blank=True, null=False)
    compromisso = models.CharField(max_length=120, blank=True, null=True)
    data_hora_inicio = models.DateTimeField(blank=True, null=True)
    data_hora_fim = models.DateTimeField(max_length=20, blank=True, null=True)
    aceitar = models.CharField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'agenda_usuario_pago'        
