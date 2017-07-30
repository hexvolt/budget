from django.conf import settings
from django.db import models
from django.utils import timezone


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

    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'conversion'
        ordering = ['date']

    @property
    def direction(self):
        return f'{self.currency_from} to {self.currency_to}'
