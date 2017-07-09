from django.db import models


class Currency(models.Model):

    name = models.CharField()
    iso_code = models.CharField()


class ExchangeRate(models.Model):

    bank = models.ForeignKey('bank.Bank')

    rate = models.DecimalField()
    date = models.DateTimeField()

    currency_from = models.ForeignKey('exchange.Currency')
    currency_to = models.ForeignKey('exchange.Currency')


class Conversion(models.Model):

    amount_from = models.DecimalField()
    account_from = models.ForeignKey('account.Account')

    amount_to = models.DecimalField()
    account_to = models.ForeignKey('account.Account')

    date = models.DateTimeField()
    description = models.CharField()
