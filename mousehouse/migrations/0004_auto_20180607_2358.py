# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-07 23:58
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mousehouse', '0003_auto_20180607_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
