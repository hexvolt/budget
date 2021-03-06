# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 18:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0002_auto_20170712_2052'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Source',
            new_name='IncomeSource',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='source',
            new_name='income_source',
        ),
        migrations.AddField(
            model_name='incomesource',
            name='user',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='income_sources',
                to=settings.AUTH_USER_MODEL
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='incomesource',
            unique_together=set([('user', 'name')]),
        ),
    ]
