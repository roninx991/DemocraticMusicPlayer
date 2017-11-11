# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-11 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20171111_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='singer',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='detail',
            name='Singer',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]