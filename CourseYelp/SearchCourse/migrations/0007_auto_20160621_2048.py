# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchCourse', '0006_coursedata_course_imag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='coursedata',
            name='tags',
            field=models.ManyToManyField(verbose_name='标签集合', to='SearchCourse.Tag', blank=True),
        ),
    ]
