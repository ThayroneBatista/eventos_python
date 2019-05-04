from .models import Evento, Pessoa_Evento_Assoc
from rest_framework import serializers

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'



class Pessoa_Evento_AssocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa_Evento_Assoc
        fields = '__all__'