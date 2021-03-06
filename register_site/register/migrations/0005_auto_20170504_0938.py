# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20170426_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermessage',
            name='team_size',
            field=models.IntegerField(choices=[(1, 1), (2, 2)], default=1),
        ),
        migrations.AddField(
            model_name='registermessage',
            name='teammate',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='registermessage',
            name='teammate_phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
