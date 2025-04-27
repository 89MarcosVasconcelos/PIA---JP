# Viewsets
from rest_framework import viewsets
# ApiView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import Quadra, Reserva
from .serializers import QuadraSerializer, ReservaSerializer

# Viewsets
class QuadraViewSet(viewsets.ModelViewSet):
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer






# ApiView
class QuadraListCreateAPIView(APIView):
    """
    Lista todas as quadras ou cria uma nova quadra.
    """

    def get(self, request):
        quadras = Quadra.objects.all()
        serializer = QuadraSerializer(quadras, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuadraSerializer(data=request.data)
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
