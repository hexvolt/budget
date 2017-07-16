from datetime import datetime

from django.conf import settings
from django.db import models


class Currency(models.Model):

    name = models.CharField(max_length=255)
    iso_code = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'currency'
        ordering = ['iso_code']

    def __str__(self):
        return f'{self.name}'


class ExchangeRate(models.Model):

    bank = models.ForeignKey('bank.Bank',
                             related_name='exchange_rates',
                             on_delete=models.CASCADE)

    rate = models.DecimalField(max_digits=18, decimal_places=9)
    date = models.DateTimeField(default=datetime.now)

    currency_from = models.ForeignKey('exchange.Currency',
                                      related_name='exchange_rates_from',
                                      on_delete=models.CASCADE)

    currency_to = models.ForeignKey('exchange.Currency',
                                    related_name='exchange_rates_to',
                                    on_delete=models.CASCADE)

    class Meta:
        db_table = 'exchange_rate'
        ordering = ['date']

    @property
    def direction(self):
        return f'{self.currency_from}/{self.currency_to}'


class Conversion(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='conversions',
                             on_delete=models.CASCADE)

    amount_from = models.DecimalField(max_digits=12, decimal_places=2)
    currency_from = models.ForeignKey('exchange.Currency',
                                      related_name='conversions_from',
                                      on_delete=models.CASCADE)

    amount_to = models.DecimalField(max_digits=12, decimal_places=2)
    currency_to = models.ForeignKey('exchange.Currency',
                                    related_name='conversions_to',
                                    on_delete=models.CASCADE)

    date = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'conversion'
        ordering = ['date']

    @property
    def direction(self):
        return f'{self.currency_from} to {self.currency_to}'
