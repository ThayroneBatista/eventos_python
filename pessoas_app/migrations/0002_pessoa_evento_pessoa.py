# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-02 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_app', '0001_initial'),
        ('pessoas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='evento_pessoa',
            field=models.ManyToManyField(to='eventos_app.Evento'),
        ),
    ]
