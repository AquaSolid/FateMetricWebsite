# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 21:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='created',
            new_name='timestamp',
        ),
    ]
