# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_auto_20180228_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='deduction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
