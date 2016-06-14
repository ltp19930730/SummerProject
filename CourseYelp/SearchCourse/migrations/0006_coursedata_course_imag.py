# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchCourse', '0005_auto_20160612_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedata',
            name='course_imag',
            field=models.FileField(blank=True, upload_to='', null=True),
        ),
    ]
