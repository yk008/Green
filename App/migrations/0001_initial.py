# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-08 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField(default=18)),
                ('gender', models.CharField(max_length=8)),
                ('salary', models.FloatField(default=10000)),
            ],
        ),
    ]
