from datetime import datetime

from django.db import models


class Income(models.Model):
    """
    Represents any kind of income user had at a certain time.

    Supposed to be filled by user. Used by system to calculate
    estimated balances and other statistics.
    """

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
