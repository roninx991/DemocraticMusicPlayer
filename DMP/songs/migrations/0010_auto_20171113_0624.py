# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 06:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0009_auto_20171113_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='slug_field',
            new_name='slug',
        ),
    ]
