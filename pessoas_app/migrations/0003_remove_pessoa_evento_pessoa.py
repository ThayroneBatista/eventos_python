# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-02 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas_app', '0002_pessoa_evento_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='evento_pessoa',
        ),
    ]