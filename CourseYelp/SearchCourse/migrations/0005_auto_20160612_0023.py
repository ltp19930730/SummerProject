# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchCourse', '0004_auto_20160609_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedata',
            name='course_homepage_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
