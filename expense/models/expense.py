from django.db import models
from django.utils import timezone


class Expense(models.Model):
    """
    Represents any kind of expense user had at a certain time.

    Supposed to be filled by user. Used by system to calculate
    estimated balances and other statistics.
    """

    expense_category = models.ForeignKey('expense.ExpenseCategory',
                                         related_name='expenses',
                                         on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey('exchange.Currency',
                                 related_name='expenses',
                                 on_delete=models.PROTECT)

    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    # from_account = models.ForeignKey('account.Account', null=True)
    # hash_tags = models.ManyToManyField()

    class Meta:
        db_table = 'expense'
        ordering = ['date']

    def __str__(self):
        return f'{self.expense_category}: {self.amount} {self.currency}'
