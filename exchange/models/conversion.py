from django.conf import settings
from django.db import models
from django.utils import timezone


class Conversion(models.Model):
    """
    Represents an operation of currency conversion performed by
    user at a certain time.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='conversions',
                             on_delete=models.CASCADE)

    amount_from = models.DecimalField(max_digits=12,
                                      decimal_places=2,
                                      help_text="Amount of money you sold")
    currency_from = models.ForeignKey('exchange.Currency',
                                      related_name='conversions_from',
                                      on_delete=models.CASCADE)

    amount_to = models.DecimalField(max_digits=12,
                                    decimal_places=2,
                                    help_text="Amount of money you purchased")
    currency_to = models.ForeignKey('exchange.Currency',
                                    related_name='conversions_to',
                                    on_delete=models.CASCADE)

    date = models.DateTimeField(default=timezone.now,
                                help_text="Date when conversion was performed")
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'conversion'
        ordering = ['date']

    @property
    def direction(self):
        return f'{self.currency_from} to {self.currency_to}'
