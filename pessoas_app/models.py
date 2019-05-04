# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pessoa(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    
    def __str__ (self):
        return self.nome