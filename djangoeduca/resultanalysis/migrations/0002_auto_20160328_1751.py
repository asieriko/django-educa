# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultanalysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
