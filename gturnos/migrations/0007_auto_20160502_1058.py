# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gturnos', '0006_auto_20160502_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='organizacion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Tipo_Usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
