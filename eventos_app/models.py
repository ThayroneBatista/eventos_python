# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pessoas_app.models import Pessoa

# Create your models here.
class Evento(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    qr_code = models.TextField()
    pessoa_evento = models.ManyToManyField(Pessoa, through='Pessoa_Evento_Assoc')

    def __str__ (self):
        return self.titulo

class Pessoa_Evento_Assoc(models.Model):
    id = models.IntegerField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento)
    presenca_confirmada = models.BooleanField(default=False)
    
    def __str__ (self):
        return 'Associacao Pessoa Evento'