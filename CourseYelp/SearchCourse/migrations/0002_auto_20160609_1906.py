# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-06-09 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchCourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedata',
            name='course_platform',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_url',
            field=models.URLField(null=True),
        ),
    ]