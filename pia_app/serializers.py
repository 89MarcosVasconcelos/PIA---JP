# quadras/serializers.py
from rest_framework import serializers
# from .models import Usuario, Quadra, Reserva
from .models import  UsuarioPago, AgendaUsuarioPago

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = '__all__'



class UsuarioPagoSerializer(serializers.ModelSerializer):
    # Removendo outros campos obrigatórios
    nome = serializers.CharField(required=True)  # Campo obrigatório
    id_pessoa = serializers.IntegerField(required=True)  # Campo obrigatório
    cpf = serializers.IntegerField(required=True)

    class Meta:
        model = UsuarioPago
        fields = ['id_pessoa', 'nome', 'cpf', 'telefone', 'preco_hora', 'celular', 'endereco', 'disponivel']  # Incluindo apenas id e nome nos campos


class AgendaUsuarioPagoSerializer(serializers.ModelSerializer):
    # quadra = QuadraSerializer(read_only=True)
    compromisso = serializers.CharField(required=True)
    id_usuario_pago = serializers.IntegerField(required=True) 
    data_hora_inicio = serializers.DateTimeField(required=True) 
    data_hora_fim = serializers.DateTimeField(required=True) 
    
    class Meta:
        model = AgendaUsuarioPago
        fields = ['compromisso','data_hora_inicio', 'data_hora_fim', 'id_usuario_pago']