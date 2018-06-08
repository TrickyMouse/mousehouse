# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mousehouse', '0004_auto_20180607_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': (('view_pg', 'Can see PG Posts'), ('view_adult', 'Can see Adult Posts'), ('view_adult_plus', 'Can see Adult Posts'))},
        ),
        migrations.AddField(
            model_name='blog',
            name='permission_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, b'PG Post'), (2, b'Adult Post'), (3, b'Adult Plus Post')], null=True),
        ),
    ]
