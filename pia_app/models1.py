from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    

class Quadra(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    tipo = models.CharField(max_length=50, choices=[('Futebol', 'Futebol'), ('Basquete', 'Basquete')])
    preco_hora = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    quadra = models.ForeignKey(Quadra, on_delete=models.CASCADE, related_name='reservas')
    nome_cliente = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Confirmada', 'Confirmada'), ('Cancelada', 'Cancelada')])

    def __str__(self):
        return f"Reserva {self.id} - {self.quadra.nome}"