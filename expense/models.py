from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'expense_category'
        ordering = ['order', 'name']


class Expense(models.Model):

    category = models.ForeignKey('expense.Category', related_name='expenses', on_delete=models.CASCADE)

    amount = models.DecimalField()
    currency = models.ForeignKey('exchange.Currency', related_name='expenses', on_delete=models.CASCADE)

    date = models.DateTimeField()
    description = models.CharField()

    # from_account = models.ForeignKey('account.Account') instead of currency???
    # hash_tags

    class Meta:
        db_table = 'expense'
        ordering = ['date']
