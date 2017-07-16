from datetime import datetime

from django.db import models


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
