# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0007_auto_20180227_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sibilings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(choices=[('child', 'Child'), ('wife', 'Wife'), ('husband', 'Husband')], default='Child', max_length=50)),
                ('full_name', models.CharField(max_length=150)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
    ]
