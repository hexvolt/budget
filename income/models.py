from django.db import models


class Source(models.Model):

    name = models.CharField()


class Income(models.Model):

    source = models.ForeignKey('income.Source')

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency')

    date = models.DateTimeField()
    description = models.CharField()

    # to_account = models.ForeignKey('account.Account')
    # hash_tags

