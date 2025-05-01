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


from datetime import datetime, date

class AgendaUsuarioPagoSerializer(serializers.ModelSerializer):
    compromisso = serializers.CharField(required=True)
    data_hora_inicio = serializers.DateTimeField(required=True)
    data_hora_fim = serializers.DateTimeField(required=True)
    id_usuario_pago = serializers.IntegerField(required=True)

    class Meta:
        model = AgendaUsuarioPago
        fields = ['compromisso', 'data_hora_inicio', 'data_hora_fim', 'id_usuario_pago']
    
    def validate(self, data):
        if data['data_hora_inicio'] >= data['data_hora_fim']:
            raise serializers.ValidationError("A data/hora de início deve ser anterior à data/hora de fim.")
        return data
   
