# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0002_auto_20170712_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='bank_accounts',
                to=settings.AUTH_USER_MODEL
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='bank',
            unique_together=set([('user', 'name')]),
        ),
    ]
