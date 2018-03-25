# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User,Job,JobFinal


@admin.register(JobFinal)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'project_name')
    list_filter = ('job_name', 'project_name')
'''
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
'''