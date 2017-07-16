from datetime import datetime

from django.conf import settings
from django.db import models


class IncomeSource(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='income_sources',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'income_source'
        unique_together = ('user', 'name')
        ordering = ['user', 'order', 'name']

    def __str__(self):
        return f'{self.name} ({self.user})'


class Income(models.Model):

    income_source = models.ForeignKey('income.IncomeSource',
                                      related_name='incomes',
                                      on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey('exchange.Currency',
                                 related_name='incomes',
                                 on_delete=models.PROTECT)

    date = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)

    # hash_tags = models.ManyToManyField()

    class Meta:
        db_table = 'income'
        ordering = ['date']

    def __str__(self):
        return f'{self.income_source}: {self.amount} {self.currency}'
