# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_auto_20170716_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incomesource',
            options={'ordering': ['user', 'order', 'name']},
        ),
    ]
