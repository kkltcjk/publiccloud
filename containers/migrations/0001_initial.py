# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]