from django.db import models


class Currency(models.Model):

    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=3)

    class Meta:
        db_table = 'currency'
        ordering = ['iso_code']


class ExchangeRate(models.Model):

    bank = models.ForeignKey('bank.Bank', related_name='exchange_rates', on_delete=models.CASCADE)

    rate = models.DecimalField()
    date = models.DateTimeField()

    currency_from = models.ForeignKey('exchange.Currency', related_name='exchange_rates', on_delete=models.CASCADE)
    currency_to = models.ForeignKey('exchange.Currency', related_name='exchange_rates', on_delete=models.CASCADE)

    class Meta:
        db_table = 'exchange_rate'
        ordering = ['date']


class Conversion(models.Model):

    account_from = models.ForeignKey('account.Account', related_name='conversions_from', on_delete=models.CASCADE)
    amount_from = models.DecimalField()

    account_to = models.ForeignKey('account.Account', related_name='conversions_to', on_delete=models.CASCADE)
    amount_to = models.DecimalField()

    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        db_table = 'conversion'
        ordering = ['date']
