# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-24 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'Platinum'), (2, 'Gold'), (3, 'Silver'), (4, 'Bronze'), (5, 'Diversity'), (6, 'Media'), (7, 'Partners'), (8, 'Coffee sponsor')], default=3)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.FileField(upload_to='sponsors/pyconcz_2018/')),
                ('description', models.TextField()),
                ('link_url', models.URLField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['level', 'name'],
            },
        ),
    ]
