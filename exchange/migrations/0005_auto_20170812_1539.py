# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0004_auto_20170730_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversion',
            name='amount_from',
            field=models.DecimalField(
                decimal_places=2,
                help_text='Amount of money you sold',
                max_digits=12
            ),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='amount_to',
            field=models.DecimalField(
                decimal_places=2,
                help_text='Amount of money you purchased',
                max_digits=12
            ),
        ),
        migrations.AlterField(
            model_name='conversion',
            name='date',
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                help_text='Date when conversion was performed'
            ),
        ),
        migrations.AlterField(
            model_name='exchangerate',
            name='rate',
            field=models.DecimalField(
                decimal_places=9,
                help_text='(currency_from / currency_to) rate',
                max_digits=18
            ),
        ),
    ]
