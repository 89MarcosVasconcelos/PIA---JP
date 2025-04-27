from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    

class UsuarioPago(models.Model):
    id_usuario_pago = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.CharField(max_length=300)
    endereco = models.TextField()
    preco_hora = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    id_pessoa = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class AgendaUsuarioPago(models.Model):
    id_agenda = models.CharField(max_length=10, primary_key=True)
    compromisso = models.CharField(max_length=300)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    id_usuario_pago = models.ForeignKey(UsuarioPago, on_delete=models.CASCADE)

    def __str__(self):
        return self.compromisso