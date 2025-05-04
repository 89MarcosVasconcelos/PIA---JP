# Viewsets
from rest_framework import viewsets
# ApiView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

# from .models import Usuario, Quadra, AgendaQuadra
from .models import   UsuarioPago, AgendaUsuarioPago
from .serializers import  UsuarioPagoSerializer, AgendaUsuarioPagoSerializer

# # Viewsets
# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer




class UsuarioPagoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPago.objects.all()
    serializer_class = UsuarioPagoSerializer

class AgendaUsuarioPagoViewSet(viewsets.ModelViewSet):
    queryset = AgendaUsuarioPago.objects.all()
    serializer_class = AgendaUsuarioPagoSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class UsuarioPagoListCreateAPIView(APIView):
    """
    Lista todos os usuariosPagos ou cria um novo usuarioPago.
    """

    # @api_view(['GET'])
    # @permission_classes([IsAuthenticated])
    def get(self, request):
        usuariosPagos = UsuarioPago.objects.all()
        serializer = UsuarioPagoSerializer(usuariosPagos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioPagoSerializer(data=request.data)
        teste = serializer.is_valid(raise_exception=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(teste, status=status.HTTP_400_BAD_REQUEST) 
        


class AgendaUsuarioPagoListCreateAPIView(APIView):
    """
    Lista todas as agendasUsuarioPago ou cria uma nova agendaUsuarioPago.
    """

    # @api_view(['GET'])
    # @permission_classes([IsAuthenticated])
    def get(self, request):
        agendasUsuarioPago = AgendaUsuarioPago.objects.all()
        serializer = AgendaUsuarioPagoSerializer(agendasUsuarioPago, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AgendaUsuarioPagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuadraDetailAPIView(APIView):
    """
    Recupera, atualiza ou deleta uma quadra específica.
    """

    def get_object(self, pk):
        try:
            return Quadra.objects.get(pk=pk)
        except Quadra.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        quadra = self.get_object(pk)
        serializer = QuadraSerializer(quadra)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Atualiza todos os campos da quadra
        """
        quadra = self.get_object(pk)
        serializer = QuadraSerializer(quadra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Atualiza apenas os campos enviados no request
        """
        quadra = self.get_object(pk)
        serializer = QuadraSerializer(quadra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quadra = self.get_object(pk)
        quadra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsuarioPagoDetailAPIView(APIView):
    """
    Recupera, atualiza ou deleta um usuarioPago específico.
    """

    def get_object(self, pk):
        try:
            return UsuarioPago.objects.get(pk=pk)
        except UsuarioPago.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        usuarioPago = self.get_object(pk)
        serializer = UsuarioPagoSerializer(usuarioPago)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Atualiza todos os campos do usuarioPago
        """
        usuarioPago = self.get_object(pk)
        serializer = UsuarioPagoSerializer(usuarioPago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Atualiza apenas os campos enviados no request
        """
        usuarioPago = self.get_object(pk)
        serializer = UsuarioPagoSerializer(usuarioPago, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        usuarioPago = self.get_object(pk)
        usuarioPago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AgendaUsuarioPagoDetailAPIView(APIView):
    """
    Recupera, atualiza ou deleta uma AgendaUsuarioPago específica.
    """

    def get_object(self, pk):
        try:
            return AgendaUsuarioPago.objects.get(pk=pk)
        except AgendaUsuarioPago.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        agenda_usuario_pago = AgendaUsuarioPago.objects.filter(id_usuario_pago=pk)  # Retorna um QuerySet
        serializer = AgendaUsuarioPagoSerializer(agenda_usuario_pago, many=True)  # Defina many=True para múltiplos objetos
        return Response(serializer.data)


    def put(self, request, pk):
        """
        Atualiza todos os campos da AgendaUsuarioPago
        """
        agendaUsuarioPago = self.get_object(pk)
        serializer = AgendaUsuarioPagoSerializer(agendaUsuarioPago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Atualiza apenas os campos enviados no request
        """
        agendaUsuarioPago = self.get_object(pk)
        serializer = AgendaUsuarioPagoSerializer(agendaUsuarioPago, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        agendaUsuarioPago = self.get_object(pk)
        agendaUsuarioPago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UsuarioPagoAllRegisterDetailAPIView(APIView):
    """
    Retorna todos os registros de UsuarioPago filtrando por id_pessoa.
    """
    def get(self, request, pk):
        usuario_pago = UsuarioPago.objects.filter(id_pessoa=pk)
        serializer = UsuarioPagoSerializer(usuario_pago, many=True)
        return Response(serializer.data)


 

# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny

# # @api_view(['POST'])
# @permission_classes([AllowAny])
# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         if not username or not password:
#             return Response({"error": "Usuário e senha são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

#         if User.objects.filter(username=username).exists():
#             return Response({"error": "Usuário já existe."}, status=status.HTTP_400_BAD_REQUEST)

#         user = User.objects.create_user(username=username, password=password)
#         return Response({"message": "Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.oauth2_backends import get_oauthlib_core




import json
from django.http import JsonResponse
from oauth2_provider.views import TokenView
from oauth2_provider.models import AccessToken
from oauthlib.oauth2.rfc6749.errors import OAuth2Error

class CustomTokenView(TokenView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            response_data = json.loads(response.content.decode('utf-8'))
            token = response_data.get("access_token")

            if token:
                access_token = AccessToken.objects.get(token=token)
                user = access_token.user
                response_data["id"] = user.id
                response_data["username"] = user.username

            return JsonResponse(response_data)
        except OAuth2Error as e:
            return JsonResponse(data=e.json, status=e.status_code)
        except Exception as e:
            return JsonResponse(data={'error': str(e)}, status=500)

# API para registro de usuários
@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterView(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Usuário e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Usuário já existe.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password, is_active=True)
    return Response({'message': 'Usuário criado com sucesso.'}, status=status.HTTP_201_CREATED)
