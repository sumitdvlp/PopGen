# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-28 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0028_auto_20171225_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobfinal',
            name='entity_three',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='filename_three',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='filetype_three',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='multiway_variables_three',
        ),
    ]
