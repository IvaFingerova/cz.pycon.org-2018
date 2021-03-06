# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-24 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='Markdown flavoured')),
                ('link', models.URLField(blank=True, default='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'get_latest_by': 'date_created',
            },
        ),
    ]
