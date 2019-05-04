"""
API endpoint.
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime  

from .models import Evento
from .serializers import EventoSerializer


#Eventos

class EventosListar(APIView):
        """
        GET: Lista todos os eventos
        POST: Adiciona um novo evento
        """
        
        def get(self, request, format=None):
            eventos = Evento.objects.order_by('data_inicio').all()
            serializer = EventoSerializer(eventos, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = EventoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoDetalhes(APIView):
        """
        GET: Lista os dados de um evento
        PUT: Atualiza o cadastro de um evento
        DELETE: Exclui o cadastro de um evento
        """
        def get_evento(self, pk):
            try:
                return Evento.objects.get(pk=pk)
            except Evento.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            evento = self.get_evento(pk)
            serializer = EventoSerializer(evento)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            evento = self.get_evento(pk)
            serializer = EventoSerializer(evento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            evento = self.get_evento(pk)
            evento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class EventosIntervalo(APIView):
    """
    GET: Retorna todos os eventos em um intervalo de tempo
        evento_entre/?date_fim=xxxx-xx-xx => Do primeiro evento ate o intervalo final
        evento_entre/?data_ini=xxxx-xx-xx => Do intervalo ate o ultimo evento
        evento_entre/?data_ini=xxxx-xx-xx&data_fim=xxxx-xx-xx => Eventos entre inicio e fim

    Para obter todos os eventos, use a url "eventos/"
    """

    def get_eventos(self, data_ini, data_fim):
        try:
            data_ini = datetime.strptime(data_ini, "%Y-%m-%d").date()
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
            return Evento.objects.order_by('data_inicio').filter(data_inicio__range=(data_ini, data_fim))
        except Evento.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        data_ini = self.request.query_params.get('data_ini', '2010-01-01')
        data_fim = self.request.query_params.get('data_fim', str(datetime.now().strftime("%Y-%m-%d")))
        eventos = self.get_eventos(data_ini, data_fim)
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)
