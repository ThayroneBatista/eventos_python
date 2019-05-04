"""
API endpoint.
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Pessoa
from .serializers import PessoaSerializer
from eventos_app.models import Pessoa_Evento_Assoc
from eventos_app.serializers import Pessoa_Evento_AssocSerializer

#Pessoas

class PessoasListar(APIView):
        """
        GET: Lista todas as pessoas
        POST: Adiciona uma nova pessoa
        """
        def get(self, request, format=None):
            pessoas = Pessoa.objects.all()
            serializer = PessoaSerializer(pessoas, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = PessoaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PessoaDetalhes(APIView):
        """
        GET: Lista os dados de uma pessoa
        PUT: Atualiza o cadastro de uma pessoa
        DELETE: Exclui o cadastro de uma pessoa
        """
        def get(self, request, pk):
            try:
                if self.request.query_params.get('eventos', None):
                    return self.get_pessoas_eventos(pk)
                return self.get_pessoas(pk)
            except Pessoa.DoesNotExist:
                raise Http404

        def put(self, request, pk, format=None):
            pessoa = self.get_pessoa(pk)
            serializer = PessoaSerializer(pessoa, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            pessoa = self.get_pessoas(pk)
            pessoa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        def get_pessoas(self, pk, format=None):
            pessoas = Pessoa.objects.get(pk=pk)
            serializer = PessoaSerializer(pessoas)
            return Response(serializer.data)
        
        def get_pessoas_eventos(self, pk, format=None):
            pessoa_evento = Pessoa_Evento_Assoc.objects.filter(pessoa=pk)
            serializer = Pessoa_Evento_AssocSerializer(pessoa_evento, many=True)
            return Response(serializer.data)
