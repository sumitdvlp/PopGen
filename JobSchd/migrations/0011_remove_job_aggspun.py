# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0010_job_geoaggsu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='AggSpUN',
        ),
    ]
