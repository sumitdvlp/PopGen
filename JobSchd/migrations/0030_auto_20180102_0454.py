# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-02 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSchd', '0029_auto_20171228_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfinal',
            name='entity_three',
            field=models.CharField(default='person', help_text='household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filename_three',
            field=models.CharField(default='hhsize_income.csv', help_text='hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filetype_three',
            field=models.CharField(default='csv', help_text='csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='entities',
            field=models.CharField(default='[household, groupquarter, person]', help_text='[household, groupquarter, person]', max_length=500, verbose_name='Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='entity_one',
            field=models.CharField(default='person', help_text='household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='filename_two',
            field=models.CharField(default='hhsize_income.csv', help_text='hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_groupquarter',
            field=models.CharField(default='', help_text='eg. [gqtotals, gqtype]', max_length=50, verbose_name='Geo Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_household',
            field=models.CharField(default='', help_text='eg. [hhtotals, hinc, hsize]', max_length=50, verbose_name='Geo Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='geo_person',
            field=models.CharField(default='', help_text='eg. [pworker, ptotals] ', max_length=50, verbose_name='Geo Person'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='housing_entities',
            field=models.CharField(default='[household, groupquarter]', help_text='[household, groupquarter]', max_length=500, verbose_name='Housing Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='ipf_tolerance',
            field=models.DecimalField(decimal_places=5, default=0.0001, max_digits=7, verbose_name='Tolerance'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='multiway_variables_two',
            field=models.CharField(default='[hsize, hinc]', help_text='[hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='person_entities',
            field=models.CharField(default='[person]', help_text='[person]', max_length=500, verbose_name='Person Entities'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='procedure',
            field=models.CharField(choices=[('IPU', 'IPU'), ('Entropy', 'Entropy')], default='IPU', max_length=50, verbose_name='Procedure'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='pvalue_tolerance',
            field=models.DecimalField(decimal_places=5, default=0.9999, max_digits=7, verbose_name='Pvalue Tolerance'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_groupquarter',
            field=models.CharField(default='', help_text='eg. [gqrtotals]', max_length=50, verbose_name='Region Groupquarter'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_household',
            field=models.CharField(default='', help_text='eg. [hhrtotals]', max_length=50, verbose_name='Region Household'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='region_person',
            field=models.CharField(default='', help_text='eg. [rpsex, rpage, rpworker, prtotals]', max_length=50, verbose_name='Region Person'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='rew_tolerance',
            field=models.DecimalField(decimal_places=5, default=0.0001, max_digits=7, verbose_name='Tolerance'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='sample_geo',
            field=models.CharField(default='geo', help_text='TAZ', max_length=50, verbose_name='Disaggregate Spatial Unit'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='zmc',
            field=models.DecimalField(decimal_places=5, default=1e-05, max_digits=7, verbose_name='Zero Marginal Correction'),
        ),
    ]
