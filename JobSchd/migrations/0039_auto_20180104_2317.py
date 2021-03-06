# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-04 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0038_auto_20180104_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_ids',
            field=models.CharField(default='[1,2,3]', help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=6000, verbose_name='Geo Ids'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_ids',
            field=models.CharField(default='[1,2,3]', help_text='For Eg. [1,2,3,4,5,6,7,8,9,10,11,12,13,14]', max_length=6000, verbose_name='Region Ids'),
        ),
    ]
