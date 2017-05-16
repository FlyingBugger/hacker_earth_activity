# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_delete_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('qq', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(blank=True, max_length=12, null=True)),
                ('campus', models.CharField(choices=[('s', '\u6c99\u6cb3\u6821\u533a'), ('q', '\u6e05\u6c34\u6cb3\u6821\u533a')], max_length=1)),
                ('grade', models.CharField(blank=True, choices=[('f', '\u5927\u4e00'), ('sf', '\u5927\u4e8c'), ('j', '\u5927\u4e09'), ('sn', '\u5927\u56db'), ('m', '\u7814\u7a76\u751f')], max_length=2, null=True, verbose_name='\u5e74\u7ea7')),
                ('major', models.CharField(blank=True, max_length=20)),
                ('prize', models.CharField(choices=[('1', '\u7b2c\u4e00\u540d'), ('2', '\u7b2c\u4e8c\u540d'), ('3', '\u7b2c\u4e09\u540d'), ('x', '\u6548\u7387\u5956')], max_length=1)),
                ('certificate', models.FileField(upload_to=b'')),
            ],
        ),
    ]
