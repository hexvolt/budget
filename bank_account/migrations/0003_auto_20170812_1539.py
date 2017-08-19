# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0002_auto_20170716_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.DecimalField(
                decimal_places=2,
                help_text='Current balance',
                max_digits=12
            ),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='name',
            field=models.CharField(
                help_text='A distinguishable name of your account '
                          '(e.g. "Visa 0XXX", "Deposit")',
                max_length=255
            ),
        ),
    ]