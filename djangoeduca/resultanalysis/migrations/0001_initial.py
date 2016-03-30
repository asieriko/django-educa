# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_es', models.TextField()),
                ('name_eu', models.TextField()),
                ('abv_es', models.TextField()),
                ('abv_eu', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='period',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_es', models.TextField()),
                ('name_eu', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('uniquename', models.TextField(primary_key=True, serialize=False)),
                ('educacode', models.TextField()),
                ('fullname', models.TextField()),
                ('birthdate', models.DateField()),
                ('gender', models.TextField(choices=[('H', 'Female'), ('M', 'Male')])),
                ('nationality', models.TextField(null=True, blank=True)),
                ('primaryschool', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name_es', models.TextField()),
                ('name_eu', models.TextField()),
                ('abv_es', models.TextField()),
                ('abv_eu', models.TextField()),
                ('course', models.ForeignKey(to='resultanalysis.course')),
            ],
        ),
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('year', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='yeardata',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('languague', models.TextField(choices=[('A', 'A'), ('AIng', 'AIng'), ('G', 'G'), ('GIng', 'GIng'), ('D', 'D')])),
                ('group', models.TextField()),
                ('repeating', models.BooleanField()),
                ('promoting', models.TextField(null=True, blank=True, choices=[('ORD', 'Ordinary Ev.'), ('EXT', 'Extraordinary Ev.'), ('AUTO', "Automatically, can't repeat"), ('NO', 'Notpromoting')])),
                ('course', models.ForeignKey(to='resultanalysis.course')),
                ('student', models.ForeignKey(to='resultanalysis.student')),
                ('year', models.ForeignKey(to='resultanalysis.year')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='period',
            field=models.ForeignKey(to='resultanalysis.period'),
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(to='resultanalysis.student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(to='resultanalysis.subject'),
        ),
        migrations.AddField(
            model_name='grade',
            name='year',
            field=models.ForeignKey(to='resultanalysis.year'),
        ),
    ]
