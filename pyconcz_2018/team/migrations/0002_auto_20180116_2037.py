# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='github',
            field=models.CharField(blank=True, help_text='just handle', max_length=255),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='photo',
            field=models.ImageField(upload_to='team/pyconcz2018/'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='twitter',
            field=models.CharField(blank=True, help_text='handle without @', max_length=255),
        ),
    ]
