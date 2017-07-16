from datetime import datetime

from django.conf import settings
from django.db import models


class ExpenseCategory(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='expense_categories',
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'expense_category'
        unique_together = ('user', 'name')
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.name}'


class Expense(models.Model):

    expense_category = models.ForeignKey('expense.ExpenseCategory',
                                         related_name='expenses',
                                         on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey('exchange.Currency',
                                 related_name='expenses',
                                 on_delete=models.PROTECT)

    date = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True)

    # from_account = models.ForeignKey('account.Account', null=True)
    # hash_tags = models.ManyToManyField()

    class Meta:
        db_table = 'expense'
        ordering = ['date']

    def __str__(self):
        return f'{self.expense_category}: {self.amount} {self.currency}'
