# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 23:29
from __future__ import unicode_literals

import JobSchd.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JobSchd', '0019_auto_20171216_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobfinal',
            old_name='entity',
            new_name='entity_one',
        ),
        migrations.RenameField(
            model_name='jobfinal',
            old_name='filename',
            new_name='filename_one',
        ),
        migrations.RenameField(
            model_name='jobfinal',
            old_name='filetype',
            new_name='filetype_one',
        ),
        migrations.RenameField(
            model_name='jobfinal',
            old_name='multiway_variables',
            new_name='multiway_variables_one',
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='Job_Pushed',
            field=models.BooleanField(default=False, help_text='If the Job is configured, Your updates will not be reflected , Make another Job', verbose_name='Is Job Is configured'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='entity_three',
            field=models.CharField(default='person', help_text='household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='entity_two',
            field=models.CharField(default='person', help_text='household or person', max_length=50, verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filename_three',
            field=models.CharField(default='hhsize_income.csv', help_text='hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filename_two',
            field=models.CharField(default='hhsize_income.csv', help_text='hhsize_income.csv', max_length=50, verbose_name='Filename'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filetype_three',
            field=models.CharField(default='csv', help_text='csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='filetype_two',
            field=models.CharField(default='csv', help_text='csv', max_length=50, verbose_name='Filetype'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo',
            field=models.CharField(default='geo', help_text='TAZ', max_length=50, verbose_name='Groupquater Entity Name'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='geo_to_sample',
            field=models.FileField(blank=True, default='geo_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='geo_to_sample'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='hid',
            field=models.CharField(default='hid', help_text='hhld', max_length=50, verbose_name='Household Entity Name'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='marginals_groupquarter',
            field=models.FileField(blank=True, help_text='groupquarters_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Marginals Groupquarter'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='marginals_household',
            field=models.FileField(blank=True, help_text='household_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Marginals Household'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='marginals_person',
            field=models.FileField(blank=True, help_text='person_marginals.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Marginals Person'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='multiway_variables_three',
            field=models.CharField(default='[hsize, hinc]', help_text='[hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='multiway_variables_two',
            field=models.CharField(default='[hsize, hinc]', help_text='[hsize, hinc]', max_length=50, verbose_name='Multiway Variables'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='pid',
            field=models.CharField(default='pid', help_text='person', max_length=50, verbose_name='Person Entity Name'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region',
            field=models.CharField(default='region', help_text='County', max_length=50, verbose_name='Aggregate Spatial Unit'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_to_geo',
            field=models.FileField(blank=True, default='region_geo_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region_to_geo'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='region_to_sample',
            field=models.FileField(blank=True, default='region_sample_mapping.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='region_to_sample'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='sample_geo',
            field=models.CharField(default='geo', help_text='TAZ', max_length=50, verbose_name='Disaggregate Spatial Unit'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='sample_groupquarter',
            field=models.FileField(blank=True, help_text='groupquarters_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Groupquarter'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='sample_household',
            field=models.FileField(blank=True, help_text='household_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Household'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='sample_person',
            field=models.FileField(blank=True, help_text='person_sample.csv', null=True, upload_to=JobSchd.models.user_directory_path, verbose_name='Sample Person'),
        ),
        migrations.AddField(
            model_name='jobfinal',
            name='synthesize',
            field=models.BooleanField(default=True, verbose_name='Synthesize'),
        ),
        migrations.AlterField(
            model_name='jobfinal',
            name='desc',
            field=models.CharField(default='Connecticut TAZ Scenario', help_text='Connecticut TAZ Scenario', max_length=50, verbose_name='Scenario Description'),
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='AggSpUN',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Agg_Geo_Mapping_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Agg_Groupquarter_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Agg_Household_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Agg_Person_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='GeoAggSU',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Geo_Groupquarter_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Geo_Household_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Geo_Person_Marginal_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Groupquarter_Sample_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='GrpQtrEn',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='HouseEN',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Household_Sample_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='PersonEN',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Person_Sample_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Sample_Agg_Mapping_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='Sample_Geo_Mapping_File',
        ),
        migrations.RemoveField(
            model_name='jobfinal',
            name='SmplSpatialUn',
        ),
        migrations.AlterUniqueTogether(
            name='jobfinal',
            unique_together=set([('user', 'job_name')]),
        ),
    ]