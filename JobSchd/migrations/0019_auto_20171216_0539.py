# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 05:39
from __future__ import unicode_literals

import JobSchd.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0018_auto_20171216_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='Household_Sample_File',
            field=models.FileField(blank=True, null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Household Sample File'),
        ),
    ]
