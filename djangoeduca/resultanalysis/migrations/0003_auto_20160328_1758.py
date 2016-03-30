# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0002_auto_20160328_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.TextField(choices=[('H', 'Female'), ('M', 'Male')], blank=True, null=True),
        ),
    ]
