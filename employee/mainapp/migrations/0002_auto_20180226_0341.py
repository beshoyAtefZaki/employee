# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='maritial_status',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=50),
        ),
    ]
