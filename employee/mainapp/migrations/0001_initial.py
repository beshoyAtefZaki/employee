# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('nationa_id', models.CharField(max_length=15, unique=True)),
                ('position', models.CharField(choices=[('X', 'Employee'), ('Y', 'Manager'), ('Z', 'CEO')], default='Employee', max_length=120)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('placr_of_birth', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('maritial_status', models.CharField(choices=[('single', 'Single'), ('female', 'Female')], default='Male', max_length=50)),
                ('gendar', models.CharField(choices=[('single', 'Single'), ('female', 'Female')], default='Male', max_length=50)),
            ],
        ),
    ]
