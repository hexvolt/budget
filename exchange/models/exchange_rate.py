from django.db import models
from django.utils import timezone


class ExchangeRate(models.Model):
    """
    Represents a currency exchange rate of a certain bank
    registered at a certain time.

    Supposed to be maintained by user or automatically.

    Having a history of exchange rates allows calculating
    all kinds of equivalents in selected currency.
    """

    bank = models.ForeignKey('bank.Bank',
                             related_name='exchange_rates',
                             on_delete=models.CASCADE)

    rate = models.DecimalField(max_digits=18,
                               decimal_places=9,
                               help_text='(currency_from / currency_to) rate')
    date = models.DateTimeField(default=timezone.now)

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
