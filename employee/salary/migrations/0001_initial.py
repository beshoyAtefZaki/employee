# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 07:28
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
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_salary', models.DecimalField(decimal_places=2, max_digits=15)),
                ('total_earnings', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15)),
                ('total_deductions', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Employee')),
            ],
        ),
    ]
