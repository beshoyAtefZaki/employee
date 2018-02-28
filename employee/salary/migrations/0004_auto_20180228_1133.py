# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_deduction_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnings', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='salary',
            name='earnings',
            field=models.ManyToManyField(blank=True, to='salary.Earnings'),
        ),
    ]
