# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]